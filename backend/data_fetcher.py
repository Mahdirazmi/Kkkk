# data_fetcher.py
# دریافت داده‌های مسابقات از یک فوتبال-API (نمونه ساختگی)
import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('FOOTBALL_API_KEY')
BASE = 'https://api.football-data.org/v2'
HEADERS = {'X-Auth-Token': API_KEY}

def fetch_matches(competition_id=2021):
    # مثال: لیگ برتر انگلیس
    url = f"{BASE}/competitions/{competition_id}/matches"
    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    data = r.json()
    rows = []
    for m in data.get('matches', []):
        rows.append({
            'utcDate': m['utcDate'],
            'homeTeam': m['homeTeam']['name'],
            'awayTeam': m['awayTeam']['name'],
            'homeGoals': m.get('score', {}).get('fullTime', {}).get('homeTeam'),
            'awayGoals': m.get('score', {}).get('fullTime', {}).get('awayTeam'),
            'status': m['status']
        })
    return pd.DataFrame(rows)

if __name__ == '__main__':
    df = fetch_matches()
    print(df.head())
