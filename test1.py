import requests
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np

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
data = pd.concat([tables[0], tables[1]], ignore_index=True)
data.rename(columns={'Team': 'TEAM'}, inplace=True)
data['TEAM'] = data['TEAM'].str.strip().str.replace('*', '', regex=False)
data['TEAM'] = data['TEAM'].apply(lambda x: team_mapping.get(x, x))

# Adding Defensive Impact
data['DefensiveImpact'] = data['oPPG'] * 1.5  # Adjusting defensive impact
print(data[['TEAM', 'PPG', 'PACE', 'oPPG', 'DefensiveImpact']].head())

# Group data and prepare for model training
average_data = data.groupby('TEAM').mean().reset_index()

# Feature Scaling
X = average_data[['PPG', 'PACE', 'DefensiveImpact']]
y = average_data['PPG']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Diagnostic check: Predict on a sample input and see the response
sample_input = np.array([[120, 105, 95 * 1.5]])  # High offensive and defensive stats
sample_input_scaled = scaler.transform(sample_input)
print("Sample input prediction:", model.predict(sample_input_scaled))

# Function to predict scores
def predict_scores(home_team, away_team, data, model, home_team_spread, total_over):
    home_data = data[data['TEAM'] == home_team]
    away_data = data[data['TEAM'] == away_team]
    if not home_data.empty and not away_data.empty:
        features_home = scaler.transform(home_data[['PPG', 'PACE', 'DefensiveImpact']])
        features_away = scaler.transform(away_data[['PPG', 'PACE', 'DefensiveImpact']])
        home_score = model.predict(features_home)
        away_score = model.predict(features_away)
        print("Predicted home score:", home_score, "Predicted away score:", away_score)
        # Additional logic here...
    else:
        print("Data missing for one or both teams.")
    return None

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
        data = response.json()['body']
        for game_key, game_info in data.items():
            home_team = team_mapping[game_info['homeTeam']]
            away_team = team_mapping[game_info['awayTeam']]
            fanduel_odds = game_info.get('fanduel', {})
            home_team_spread = float(fanduel_odds.get('homeTeamSpread'))
            total_over = float(fanduel_odds.get('totalOver'))
            result = predict_scores(home_team, away_team, average_data, model, home_team_spread, total_over)
            if result:
                print(f"Game ID: {game_key}")
                print(f"Away Team: {away_team} - Predicted Score: {result['away_score']}")
                print(f"Home Team: {home_team} - Predicted Score: {result['home_score']}")
                print(f"Combined Total Score: {result['total_score']} - Total: {result['total_result']}")
                print(f"Spread Result: {result['spread_result']}")
    else:
        print("Failed to fetch data:", response.status_code)

# Example usage
get_nba_betting_odds()


# Usage example
predict_scores('Chicago', 'Los Angeles', average_data, model, -5.5, 215.5)
