import pandas as pd
import numpy as np
import requests
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('nba-project.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("NBA Model").sheet1

# Example of how to write a row to the spreadsheet
def update_sheet(result):
    row = [result['Game ID'], result['Away Team'], result['Away Score'], result['Home Team'], result['Home Score'],
           result['Total Score'], result['Over/Under'], result['Suggested Bet'], result['FanDuel Spread'], result['FanDuel Total']]
    index = 2  # Starting from the second row
    sheet.insert_row(row, index)

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

# Apply team mapping
regular_season_data['Team'] = regular_season_data['TEAM'].apply(lambda x: team_mapping.get(x.strip(), x))
playoff_data['Team'] = playoff_data['TEAM'].apply(lambda x: team_mapping.get(x.strip(), x))

# Print column names to verify
print("Column names in regular season data:", regular_season_data.columns)
print("Column names in playoff data:", playoff_data.columns)

# Combine and calculate average data
combined_data = pd.concat([regular_season_data, playoff_data])

# Exclude non-numeric columns before calculating the mean
numeric_columns = combined_data.select_dtypes(include=[np.number])
average_data = numeric_columns.groupby(combined_data['TEAM']).mean().reset_index()

# Prepare the data for the model
X = average_data[['PPG', 'oPPG', 'PACE']]
y = average_data['PPG']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict function using the model
def predict_scores(home_team, away_team, average_data, model, scaler, home_team_spread, total_over):
    home_data = average_data[average_data['TEAM'] == home_team]
    away_data = average_data[average_data['TEAM'] == away_team]
    if not home_data.empty and not away_data.empty:
        features_home = scaler.transform(home_data[['PPG', 'oPPG', 'PACE']])
        features_away = scaler.transform(away_data[['PPG', 'oPPG', 'PACE']])
        home_score = model.predict(features_home)
        away_score = model.predict(features_away)

        total_score = home_score + away_score
        over_under = "Over" if total_score > total_over else "Under"
        spread_result = f"Bet on {home_team}" if (home_score - away_score) < home_team_spread else f"Bet on {away_team}"
        
        return {
            'Game ID': "",  # This will be set in get_nba_betting_odds
            'Home Team': home_team,
            'Away Team': away_team,
            'Home Score': round(home_score[0], 0),
            'Away Score': round(away_score[0], 0),
            'Total Score': round(total_score[0], 0),
            'Suggested Bet': spread_result,
            'Over/Under': over_under,
            'FanDuel Spread': home_team_spread,
            'FanDuel Total': total_over
        }
    else:
        return "Data missing for one or both teams."


def get_nba_betting_odds():
    today = datetime.now().strftime("%Y%m%d")
    url = "https://tank01-fantasy-stats.p.rapidapi.com/getNBABettingOdds"
    print("Querying data for:", today)
    querystring = {"gameDate": '20240505'}
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
            total_over = float(fanduel_odds.get('totalOver', 0))
            result = predict_scores(home_team, away_team, average_data, model, scaler, home_team_spread, total_over)
            if isinstance(result, dict):  # Ensure result is a dictionary
                result['Game ID'] = game_key
                print(f"Game ID: {game_key}")
                print(f"Away Team: {away_team}, Predicted Score: {result['Away Score']}")
                print(f"Home Team: {home_team}, Predicted Score: {result['Home Score']}")
                print(f"Total Predicted Score: {result['Total Score']}, {result['Over/Under']}")
                print(f"Suggested Bet: {result['Suggested Bet']}")
                print(f"FanDuel Spread: {result['FanDuel Spread']}, FanDuel Total: {result['FanDuel Total']}")
                update_sheet(result)  # Update the Google Sheet with the result
    else:
        print("Failed to fetch data:", response.status_code)

get_nba_betting_odds()
