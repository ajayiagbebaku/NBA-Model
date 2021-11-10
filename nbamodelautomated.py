import pandas as pd
import streamlit as st
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = "https://www.basketball-reference.com/leagues/NBA_2022.html#all_advanced_team"

df = pd.read_html(url,header=1)

advanced_stats = (df[10])
advanced_stats.drop('Unnamed: 17', axis=1, inplace=True)
advanced_stats.drop('Unnamed: 22', axis=1 ,inplace=True)
advanced_stats.drop('Unnamed: 27', axis=1 ,inplace=True)

advanced_stats.to_csv("advancedStats.csv", index=False)

columns = ['Team','ORtg', 'DRtg', 'Pace']
advanced_stats_clean = advanced_stats[columns]
advanced_stats_records = advanced_stats_clean.values.tolist()
print(advanced_stats_records)

DRIVER = 'SQL Server'
SERVER_NAME =''
DATABASE_NAME = ''

def connection_string()







