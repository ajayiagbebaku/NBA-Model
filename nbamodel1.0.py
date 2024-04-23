import pandas as pd
import requests
from bs4 import BeautifulSoup

# Function to scrape data using BeautifulSoup
def scrape_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')  # Find all tables
        if tables:
            return pd.read_html(str(tables[0]))[0]  # Assuming the first table is the correct one
        else:
            print("No tables found on the page.")
            return None
    else:
        print(f"Failed to access {url}")
        return None

# URLs
team_ppg_url = "https://www.teamrankings.com/nba/stat/points-per-game"
team_opp_ppg_url = "https://www.teamrankings.com/nba/stat/opponent-points-per-game"
win_scores_url = "https://www.teamrankings.com/nba/player-stat/win-score"

# Scrape data
team_ppg_data = scrape_data(team_ppg_url)
team_opp_ppg_data = scrape_data(team_opp_ppg_url)
win_scores_data = scrape_data(win_scores_url)

# Display the first few rows of the data if available
if team_ppg_data is not None:
    print(team_ppg_data.head())
if team_opp_ppg_data is not None:
    print(team_opp_ppg_data.head())
if win_scores_data is not None:
    print(win_scores_data.head())
