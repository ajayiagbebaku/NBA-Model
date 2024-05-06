import pandas as pd
import requests
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from datetime import datetime

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
nba_data = pd.concat([tables[0], tables[1]], ignore_index=True)  # Rename to nba_data for clarity
nba_data.rename(columns={'Team': 'TEAM'}, inplace=True)
nba_data['TEAM'] = nba_data['TEAM'].str.strip().str.replace('*', '', regex=False)
nba_data['TEAM'] = nba_data['TEAM'].apply(lambda x: team_mapping.get(x, x))

# Prepare the data for the model
X = nba_data[['PPG', 'oPPG', 'PACE']]
y = nba_data['PPG']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict function using the model
def predict_scores(home_team, away_team, nba_data, model, scaler, home_team_spread, total_over):
    home_data = nba_data[nba_data['TEAM'] == home_team]
    away_data = nba_data[nba_data['TEAM'] == away_team]
    if not home_data.empty and not away_data.empty:
        features_home = scaler.transform(home_data[['PPG', 'oPPG', 'PACE']])
        features_away = scaler.transform(away_data[['PPG', 'oPPG', 'PACE']])
        home_score = model.predict(features_home)
        away_score = model.predict(features_away)
        return {'Home Score': home_score[0], 'Away Score': away_score[0]}
    else:
        return "Data missing for one or both teams."

def get_nba_betting_odds():
    today = datetime.now().strftime("%Y%m%d")  # Format the date as YYYYMMDD
    url = "https://tank01-fantasy-stats.p.rapidapi.com/getNBABettingOdds"
    print(today)
    querystring = {"gameDate": today}
    headers = {
        "X-RapidAPI-Key": "2d2c1f1b92msh6a8546438f75ab7p18f644jsnfa55639522ed",
        "X-RapidAPI-Host": "tank01-fantasy-stats.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        betting_data = response.json()['body']
        for game_key, game_info in betting_data.items():
            home_team = team_mapping[game_info['homeTeam']]
            away_team = team_mapping[game_info['awayTeam']]
            fanduel_odds = game_info.get('fanduel', {})
            home_team_spread = float(fanduel_odds.get('homeTeamSpread', 0))  # Default to 0 if not found
            total_over = float(fanduel_odds.get('totalOver', 0))  # Default to 0 if not found
            result = predict_scores(home_team, away_team, nba_data, model, scaler, home_team_spread, total_over)
            if result:
                print(f"Game ID: {game_key}")
                print(f"Away Team: {away_team} - Predicted Score: {result['Away Score']}")
                print(f"Home Team: {home_team} - Predicted Score: {result['Home Score']}")
    else:
        print("Failed to fetch data:", response.status_code)

# Example usage
get_nba_betting_odds()
