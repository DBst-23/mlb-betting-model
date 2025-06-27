
import pandas as pd

# Load player stats
df = pd.read_csv("player_stats.csv")

# Show top 5 players by xwOBA
top_hitters = df.sort_values("xwOBA", ascending=False).head()
print("Top Hitters by xwOBA:")
print(top_hitters)
