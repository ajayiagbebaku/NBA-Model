import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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
data.rename(columns={'Team': 'TEAM', 'PPG': 'PPG', 'OPPG': 'oPPG', 'Pace': 'PACE'}, inplace=True)
data['TEAM'] = data['TEAM'].str.strip().str.replace('*', '', regex=False)
data['TEAM'] = data['TEAM'].apply(lambda x: team_mapping.get(x, x))
average_data = data.groupby('TEAM').agg({'PPG': 'mean', 'oPPG': 'mean', 'PACE': 'mean'}).reset_index()

# Train the model
X = average_data[['PPG', 'oPPG', 'PACE']]
y = average_data['PPG']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Function to fetch and preprocess player data
def fetch_player_data():
    player_stats_url = 'https://www.teamrankings.com/nba/player-stat/win-score'
    player_data = pd.read_html(player_stats_url)[0]
    player_data = player_data[['Player', 'Team', 'Value']]  # Keep only relevant columns
    return player_data

player_data = fetch_player_data()
print(player_data.head())

# Reverse the team mapping to convert full names to codes
reverse_team_mapping = {v: k for k, v in team_mapping.items()}

# Adjust team names in player data to match team codes
def adjust_team_names(player_data, reverse_mapping):
    player_data['Team'] = player_data['Team'].apply(lambda x: reverse_mapping.get(x, x))
    return player_data

player_data = adjust_team_names(player_data, reverse_team_mapping)
print(player_data.head())

def adjust_for_injuries(team_score, injured_players, player_data):
    total_injury_impact = 0
    for player in injured_players:
        player_row = player_data[player_data['Player'] == player]
        if not player_row.empty:
            win_score = player_row['Value'].iloc[0] / 4  # Adjust the divisor based on your scoring system
            total_injury_impact += win_score
        else:
            print(f"No matching data found for player '{player}'. Check player name.")
    return team_score - total_injury_impact

# Example of using injury adjustments in predictions
def get_injured_players():
    injured_players = {}
    num_teams = int(input("Enter the number of teams with injuries today: "))
    for _ in range(num_teams):
        team = input("Enter the team name: ")
        players = input("Enter the injured players for this team (comma-separated): ").split(',')
        injured_players[team] = [player.strip() for player in players]
    return injured_players


# Collect injuries interactively
injured_players = get_injured_players()  # This will be a dictionary mapping teams to lists of injured players

# You would then use `injured_players` to adjust scores in your game predictions, based on the data you've fetched and processed.


def predict_scores(home_team, away_team, data, model, home_team_spread, total_over):
    home_data = data[data['TEAM'] == home_team]
    away_data = data[data['TEAM'] == away_team]
    if not home_data.empty and not away_data.empty:
        home_advantage = 3  # Home advantage points
        features_home = home_data[['PPG', 'oPPG', 'PACE']].to_numpy().reshape(1, -1)
        features_away = away_data[['PPG', 'oPPG', 'PACE']].to_numpy().reshape(1, -1)
        home_score = model.predict(features_home) + home_advantage
        away_score = model.predict(features_away)
        total_score = home_score + away_score
        
        # Round scores to the nearest whole number
        home_score = round(home_score[0], 0)
        away_score = round(away_score[0], 0)
        total_score = round(total_score[0], 0)
        
        # Determine if home team covers the spread
        if (home_score - away_score) > home_team_spread:
            spread_result = f"{home_team} covers"
        else:
            spread_result = f"{home_team} does not cover"
        
        # Determine if the total score is over or under
        if total_score > total_over:
            total_result = "Over"
        else:
            total_result = "Under"
        
        result = {
            'home_score': home_score,
            'away_score': away_score,
            'total_score': total_score,
            'spread_result': spread_result,
            'total_result': total_result
        }
        return result
    return None
def get_nba_betting_odds(game_date):
    url = "https://tank01-fantasy-stats.p.rapidapi.com/getNBABettingOdds"
    querystring = {"gameDate": game_date}
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
                print("-----")
    else:
        print("Failed to fetch data:", response.status_code)

# Example usage
get_nba_betting_odds("20240502")