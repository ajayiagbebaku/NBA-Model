import pandas as pd
import numpy as np
import requests
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Initialize Google Drive and Sheets API client
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('nba-project.json', scope)
client = gspread.authorize(creds)
sheet = client.open("NBA Model").sheet1

# Define the function to update Google Sheets
def update_sheet(result):
    row = [result['Game ID'], result['Away Team'], result['Away Score'], result['Home Team'], result['Home Score'],
           result['Total Score'], result['Over/Under'], result['Suggested Bet'], result['FanDuel Spread Home'], result['FanDuel Total']]
    sheet.insert_row(row, 2)
    print("Updated sheet completed")

# Team code to full name mapping
team_mapping = {
    'ATL': 'Atlanta', 'BOS': 'Boston', 'BKN': 'Brooklyn', 'CHA': 'Charlotte', 'CHI': 'Chicago',
    'CLE': 'Cleveland', 'DAL': 'Dallas', 'DEN': 'Denver', 'DET': 'Detroit', 'GSW': 'Golden State',
    'HOU': 'Houston', 'IND': 'Indiana', 'LAC': 'LA Clippers', 'LAL': 'LA Lakers', 'MEM': 'Memphis',
    'MIA': 'Miami', 'MIL': 'Milwaukee', 'MIN': 'Minnesota', 'NOP': 'New Orleans', 'NY': 'New York',
    'OKC': 'Oklahoma City', 'ORL': 'Orlando', 'PHI': 'Philadelphia', 'PHX': 'Phoenix', 'POR': 'Portland',
    'SAC': 'Sacramento', 'SAS': 'San Antonio', 'TOR': 'Toronto', 'UTA': 'Utah', 'WAS': 'Washington'
}

# Load and preprocess team stats data
url = 'https://www.nbastuffer.com/2023-2024-nba-team-stats/'
tables = pd.read_html(url)
regular_season_data = tables[1]
playoff_data = tables[0]

# Map team names
regular_season_data['TEAM'] = regular_season_data['TEAM'].map(lambda x: team_mapping.get(x.strip(), x))
playoff_data['TEAM'] = playoff_data['TEAM'].map(lambda x: team_mapping.get(x.strip(), x))

# Combine data and calculate averages
combined_data = pd.concat([regular_season_data, playoff_data])
numeric_columns = combined_data.select_dtypes(include=[np.number])
average_data = numeric_columns.groupby(combined_data['TEAM']).mean().reset_index()

# Scale and split the dataset
X = average_data[['PPG', 'oPPG', 'PACE']]
y = average_data['PPG']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=100)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)


# Function to predict scores and determine bets
def predict_scores(home_team, away_team, average_data, model, scaler, home_team_spread, away_team_spread, total_over, playoff=True):
    home_data = average_data[average_data['TEAM'] == home_team].copy()
    away_data = average_data[average_data['TEAM'] == away_team].copy()

    # Apply playoff adjustments if playoff is True
    if playoff:
        home_data['oPPG'] *= 1.5 # Increase the opponent's PPG by 20% during playoffs
        away_data['oPPG'] *= 1.5
        print(home_data)
        print(away_data)

    if not home_data.empty and not away_data.empty:
        # Print oPPG values before scaling for comparison
        print("Original Home oPPG:", home_data['oPPG'].iloc[0])
        print("Original Away oPPG:", away_data['oPPG'].iloc[0])

        features_home = scaler.transform(home_data[['PPG', 'oPPG', 'PACE' ]])
        features_away = scaler.transform(away_data[['PPG', 'oPPG', 'PACE']])
        home_score = model.predict(features_home)
        away_score = model.predict(features_away)
        print(home_score)
        print(away_score)

        # Print scaled oPPG values (they are in the second column of the features arrays)
        print("Scaled Home oPPG:", features_home[0][1])  # Index 1 is the oPPG in your feature set
        print("Scaled Away oPPG:", features_away[0][1])

        projected_diff = home_score - away_score

        # Determine which team to bet on
        if home_team_spread < 0:  # Home team is the favorite
            suggested_bet = f"Bet on {home_team}" if projected_diff > abs(home_team_spread) else f"Bet on {away_team}"
        else:  # Away team is the favorite
            suggested_bet = f"Bet on {away_team}" if -projected_diff > abs(away_team_spread) else f"Bet on {home_team}"
        
        return {
            'Game ID': "",
            'Home Team': home_team,
            'Away Team': away_team,
            'Home Score': round(home_score[0], 0),
            'Away Score': round(away_score[0], 0),
            'Total Score': round((home_score + away_score)[0], 0),
            'Suggested Bet': suggested_bet,
            'Over/Under': "Over" if (home_score + away_score) > total_over else "Under",
            'FanDuel Spread Home': home_team_spread,
            'FanDuel Total': total_over
        }
    else:
        return "Data missing for one or both teams."



# Main function to fetch NBA betting odds and update sheet
def get_nba_betting_odds():
    today = datetime.now().strftime("%Y%m%d")
    url = "https://tank01-fantasy-stats.p.rapidapi.com/getNBABettingOdds"
    print("Querying data for:", today)
    querystring = {"gameDate": today}
    headers = {
        "X-RapidAPI-Key": "2d2c1f1b92msh6a8546438f75ab7p18f644jsnfa55639522ed",
        "X-RapidAPI-Host": "tank01-fantasy-stats.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        betting_data = response.json()['body']
        for game_key, game_info in betting_data.items():
            home_team = team_mapping.get(game_info['homeTeam'], game_info['homeTeam'])
            away_team = team_mapping.get(game_info['awayTeam'], game_info['awayTeam'])
            fanduel_odds = game_info.get('fanduel', {})
            home_team_spread = float(fanduel_odds.get('homeTeamSpread', 0))
            away_team_spread = -home_team_spread
            total_over = float(fanduel_odds.get('totalOver', 0))
            result = predict_scores(home_team, away_team, average_data, model, scaler, home_team_spread, away_team_spread, total_over, playoff=True)
            if isinstance(result, dict):
                result['Game ID'] = game_key
                update_sheet(result)
    else:
        print("Failed to fetch data:", response.status_code)

get_nba_betting_odds()
