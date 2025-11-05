
import pandas as pd
from src.data_bootloader import load_nba_team_factors# Load player stats
df = pd.read_csv("player_stats.csv")

# === Load NBA team factors (CraftedNBA feed) ===
team_factors = load_nba_team_factors(base_dir="./data", max_age_days=3)
print(f"✅ Loaded {len(team_factors)} NBA team factor rows.")
print(team_factors.head())# Show top 5 players by xwOBA
top_hitters = df.sort_values("xwOBA", ascending=False).head()
print("Top Hitters by xwOBA:")
print(top_hitters)
