# src/data_bootloader.py
from __future__ import annotations
import os, glob, datetime as dt
import pandas as pd

class StaleDataWarning(UserWarning):
    pass

def _latest_snapshot(proc_dir: str, prefix="nba_team_factors_") -> str | None:
    paths = sorted(glob.glob(os.path.join(proc_dir, f"{prefix}[0-9]*.csv")))
    return paths[-1] if paths else None

def load_nba_team_factors(base_dir: str = "./data", max_age_days: int = 3) -> pd.DataFrame:
    """
    Loads team factors produced by import_craftednba.py.
    Priority:
      1) processed/nba_team_factors_current.csv
      2) latest processed/nba_team_factors_YYYYMMDD.csv
    Warn if data older than max_age_days.
    """
    proc_dir = os.path.join(base_dir, "processed")
    current = os.path.join(proc_dir, "nba_team_factors_current.csv")
    path = current if os.path.exists(current) else _latest_snapshot(proc_dir)
    if not path:
        raise FileNotFoundError("No team factors found. Run import_craftednba.py first.")

    df = pd.read_csv(path)

    # staleness check
    stamp = None
    if path.endswith("current.csv"):
        snap = _latest_snapshot(proc_dir)
        if snap:
            stamp = snap.split("_")[-1].split(".")[0]  # YYYYMMDD
    else:
        stamp = path.split("_")[-1].split(".")[0]  # YYYYMMDD

    if stamp and stamp.isdigit():
        y, m, d = int(stamp[:4]), int(stamp[4:6]), int(stamp[6:])
        age = (dt.date.today() - dt.date(y, m, d)).days
        if age > max_age_days:
            import warnings
            warnings.warn(
                f"NBA team factors are {age} days old (>{max_age_days}). Refresh recommended.",
                StaleDataWarning
            )

    # minimal schema assertion (case-insensitive)
    req = {
        "team","ortg","drtg","netrtg",
        "off_efg","off_orb","off_tov","off_ftar",
        "def_efg","def_orb","def_tov","def_ftar"
    }
    have = {c.lower() for c in df.columns}
    missing = req - have
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df
