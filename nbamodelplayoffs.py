import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load and preprocess data
url = 'https://www.nbastuffer.com/2023-2024-nba-team-stats/'
tables = pd.read_html(url)
data = pd.concat([tables[0], tables[1]], ignore_index=True)

# Fetch player data
player_stats_url = 'https://www.teamrankings.com/nba/player-stat/win-score'
player_data = pd.read_html(player_stats_url)[0]
player_data = player_data[['Player', 'Team', 'Value']] 

# Print a sample of the player data to verify
print(player_data.head())

# Rename and clean data
data.rename(columns={'Team': 'TEAM', 'PPG': 'PPG', 'OPPG': 'oPPG', 'Pace': 'PACE'}, inplace=True)
data['TEAM'] = data['TEAM'].str.strip().str.replace('*', '', regex=False)

# Combine and average the data
average_data = data.groupby('TEAM').agg({'PPG': 'mean', 'oPPG': 'mean', 'PACE': 'mean'}).reset_index()

# Model features and target
X = average_data[['PPG', 'oPPG', 'PACE']]
y = average_data['PPG']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Function to adjust for injuries
def adjust_for_injuries(team_score, injured_players, player_data):
    if not injured_players:
        return team_score  # Return the original score if no players are listed as injured
    total_injury_impact = 0
    for player in injured_players:
        player_row = player_data[player_data['Player'] == player]
        if not player_row.empty:
            win_score = player_row['Value'].iloc[0] / 4
            total_injury_impact += win_score
        else:
            print(f"No matching data found for player '{player}'. Check player name.")
    return team_score - total_injury_impact

# Prediction function
def predict_scores(home_team, away_team, data, model):
    home_data = data[data['TEAM'] == home_team]
    away_data = data[data['TEAM'] == away_team]
    if not home_data.empty and not away_data.empty:
        home_advantage = 3
        features_home = home_data[['PPG', 'oPPG', 'PACE']].to_numpy().reshape(1, -1)
        features_away = away_data[['PPG', 'oPPG', 'PACE']].to_numpy().reshape(1, -1)
        home_score = model.predict(features_home) + home_advantage
        away_score = model.predict(features_away)
        return home_score[0], away_score[0]
    return None, None

def adjust_for_injuries(team_score, injured_players, player_data):
    if not injured_players:
        return team_score  # Return the original score if no players are listed as injured
    total_injury_impact = 0
    for player in injured_players:
        player_row = player_data[player_data['Player'] == player]
        if not player_row.empty:
            win_score = player_row['Value'].iloc[0] / 4
            total_injury_impact += win_score
        else:
            print(f"No matching data found for player '{player}'. Check player name.")
    return team_score - total_injury_impact

def calculate_implied_probability(odds):
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return abs(odds) / (abs(odds) + 100)

def make_betting_decision(home_team, away_team, home_injured, away_injured, spread, spread_odds, over_under, over_under_odds, data, model, player_data):
    home_score_pred, away_score_pred = predict_scores(home_team, away_team, data, model)
    # Set fixed odds
    spread_odds = -110
    over_under_odds = -110
    
    # Adjust scores for injuries
    home_score_pred = adjust_for_injuries(home_score_pred, home_injured, player_data)
    away_score_pred = adjust_for_injuries(away_score_pred, away_injured, player_data)

    # Apply playoff adjustments with defensive emphasis
    home_score_pred, away_score_pred = adjust_for_playoffs(home_score_pred, away_score_pred, 5, 5, 4, 4, 3)

    predicted_diff = home_score_pred - away_score_pred
    predicted_total = home_score_pred + away_score_pred

    spread_bet = 'Home' if predicted_diff > spread else 'Away'
    over_under_bet = 'Over' if predicted_total > over_under else 'Under'

    # Calculate implied probabilities
    spread_probability = calculate_implied_probability(spread_odds) * 100
    over_under_probability = calculate_implied_probability(over_under_odds) * 100

    return (f"Projected Playoff Scores: {home_team} {home_score_pred:.2f}, {away_team} {away_score_pred:.2f}\n"
            f"Spread Bet: Bet on the {spread_bet} team (Implied Probability: {spread_probability:.2f}%), "
            f"Over/Under: Bet {over_under_bet} (Implied Probability: {over_under_probability:.2f}%) "
            f"(Total predicted: {predicted_total:.2f})")



def adjust_for_playoffs(home_score, away_score, star_player_home, star_player_away, defense_home, defense_away, home_court_advantage):
    # Increased emphasis on defense in the playoffs
    defensive_adjustment_factor = 3  # Modify this factor to increase or decrease defensive impact

    # Apply adjustments: Subtract for defense to lower the scores
    home_score += (star_player_home * 1.2 + home_court_advantage) - (defense_home * defensive_adjustment_factor)
    away_score += (star_player_away * 1.2) - (defense_away * defensive_adjustment_factor)
    
    return home_score, away_score



# Prompt user inputs for game details, odds, and injuries
home_team = input("Enter the home team: ")
away_team = input("Enter the away team: ")
home_injured = input("Enter injured players for the home team, separated by commas (if any): ").split(',')
away_injured = input("Enter injured players for the away team, separated by commas (if any): ").split(',')
spread = float(input("Enter the FanDuel spread for the home team: "))
over_under = float(input("Enter the FanDuel over/under number for total points: "))

# Make and display the betting decision
betting_decision = make_betting_decision(home_team, away_team, home_injured, away_injured, spread, spread_odds, over_under, over_under_odds, average_data, model, player_data)
print(betting_decision)
