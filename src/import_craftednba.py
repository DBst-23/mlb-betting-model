#!/usr/bin/env python3
"""
CraftedNBA Four Factors Importer
--------------------------------
Ingest a team-level export from CraftedNBA (or a copy/paste to CSV),
normalize fields, and emit model-ready files.

Usage:
  python import_craftednba.py --input data/raw/craftednba_four_factors_YYYYMMDD.csv --date 2025-11-05 --outdir ./data

Outputs (in --outdir):
  processed/nba_team_factors_current.csv
  processed/nba_team_factors_YYYYMMDD.csv
  processed/nba_team_factors_YYYYMMDD.json
"""

import argparse, os, sys, json, datetime
import pandas as pd

TEAM_ABBR = {
    "Atlanta Hawks": "ATL", "Boston Celtics": "BOS", "Brooklyn Nets": "BKN",
    "Charlotte Hornets": "CHA", "Chicago Bulls": "CHI", "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL", "Denver Nuggets": "DEN", "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW", "Houston Rockets": "HOU", "Indiana Pacers": "IND",
    "LA Clippers": "LAC", "Los Angeles Clippers": "LAC", "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM", "Miami Heat": "MIA", "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN", "New Orleans Pelicans": "NOP", "New York Knicks": "NYK",
    "Oklahoma City Thunder": "OKC", "Orlando Magic": "ORL", "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHX", "Portland Trail Blazers": "POR", "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS", "Toronto Raptors": "TOR", "Utah Jazz": "UTA", "Washington Wizards": "WAS"
}

ALIASES = {
    "team": ["team", "Team", "TEAM", "squad", "franchise"],
    "ORTG": ["ORTG", "OffRtg", "ORtg", "Offensive Rating"],
    "DRTG": ["DRTG", "DefRtg", "DRtg", "Defensive Rating"],
    "NetRTG": ["NetRTG", "Net Rtg", "Net Rating", "Net"],
    "Off_eFG": ["EFG%", "eFG%", "Off eFG%", "EFG_off", "EFG_offense", "Offense eFG%"],
    "Off_ORB": ["ORB%", "Off ORB%", "ORB_off", "ORB% (Off)"],
    "Off_FTAr": ["FTAr", "FTA Rate", "FT Rate (Off)"],
    "Off_TOV": ["TO%", "TOV%", "TOV_off", "TO% (Off)", "Turnover%"],
    "Def_eFG": ["EFG% (Def)", "Def eFG%", "eFG%_def", "eFG% Allowed"],
    "Def_ORB": ["ORB% (Def)", "Def ORB%", "Opp ORB%", "ORB%_def"],
    "Def_FTAr": ["FTAr (Def)", "Def FTAr", "Opp FTAr", "FT Rate (Def)"],
    "Def_TOV": ["TO% (Def)", "Def TOV%", "TOV%_def", "Opp TOV% Forced"]
}

def find_column(df, aliases):
    for a in aliases:
        if a in df.columns:
            return a
        for col in df.columns:
            if col.strip().lower() == a.strip().lower():
                return col
    return None

def pct_to_float(x):
    """Convert percent strings/numbers to 0–1 floats."""
    if pd.isna(x): return None
    if isinstance(x, str):
        s = x.strip().replace('%', '')
        if s == '': return None
        try: val = float(s)
        except: return None
    else:
        val = float(x)
    if 0 <= val <= 1.5: return val
    return val / 100.0

def ratio_to_float(x):
    """Normalize FTAr as a ratio (not percent)."""
    if pd.isna(x): return None
    if isinstance(x, str):
        s = x.strip().replace('%', '')
        if s == '': return None
        try: val = float(s)
        except: return None
    else:
        val = float(x)
    if val > 1.5: return val / 100.0
    return val

def load_and_normalize(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    cols = {}
    for canon, alias_list in ALIASES.items():
        col = find_column(df, alias_list)
        if col is None and canon == "NetRTG":
            pass
        elif col is None:
            raise ValueError(f"Missing required column for {canon}. Acceptable aliases: {alias_list}")
        cols[canon] = col

    out = pd.DataFrame()
    out["team_name"] = df[cols.get("team", "team")]
    out["team"] = out["team_name"].map(TEAM_ABBR).fillna(out["team_name"])
    out["ortg"] = pd.to_numeric(df[cols["ORTG"]], errors="coerce")
    out["drtg"] = pd.to_numeric(df[cols["DRTG"]], errors="coerce")
    if cols.get("NetRTG"):
        out["netrtg"] = pd.to_numeric(df[cols["NetRTG"]], errors="coerce")
    else:
        out["netrtg"] = out["ortg"] - out["drtg"]

    # Normalize four factors
    out["off_efg"]  = df[cols["Off_eFG"]].apply(pct_to_float)
    out["off_orb"]  = df[cols["Off_ORB"]].apply(pct_to_float)
    out["off_tov"]  = df[cols["Off_TOV"]].apply(pct_to_float)
    out["off_ftar"] = df[cols["Off_FTAr"]].apply(ratio_to_float)
    out["def_efg"]  = df[cols["Def_eFG"]].apply(pct_to_float)
    out["def_orb"]  = df[cols["Def_ORB"]].apply(pct_to_float)
    out["def_tov"]  = df[cols["Def_TOV"]].apply(pct_to_float)
    out["def_ftar"] = df[cols["Def_FTAr"]].apply(ratio_to_float)

    # Bound values
    for c in ["off_efg","def_efg","off_orb","def_orb","off_tov","def_tov"]:
        out[c] = out[c].clip(lower=0, upper=1)
    for c in ["off_ftar","def_ftar"]:
        out[c] = out[c].clip(lower=0, upper=1.5)

    out["source"] = "CraftedNBA"
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--outdir", default="./data")
    args = ap.parse_args()

    df = load_and_normalize(args.input)

    proc_dir = os.path.join(args.outdir, "processed")
    os.makedirs(proc_dir, exist_ok=True)

    stamp = args.date.replace("-", "")
    csv_current = os.path.join(proc_dir, "nba_team_factors_current.csv")
    csv_snapshot = os.path.join(proc_dir, f"nba_team_factors_{stamp}.csv")
    json_snapshot = os.path.join(proc_dir, f"nba_team_factors_{stamp}.json")

    df_out = df.sort_values("team").reset_index(drop=True)
    df_out.to_csv(csv_current, index=False)
    df_out.to_csv(csv_snapshot, index=False)
    df_out.to_json(json_snapshot, orient="records", indent=2)

    print(f"[OK] CraftedNBA import complete for {args.date}")
    print(f"Rows: {len(df_out)} | Sample teams: {', '.join(df_out['team'].head(5))}")
    print(f"Wrote:\n  - {csv_current}\n  - {csv_snapshot}\n  - {json_snapshot}")

if __name__ == "__main__":
    main()
