import json
import pandas as pd
from typing import List, Dict

from pandas import DataFrame

GUIDE_PATH = "arcane_burst_guide_aoe.json"


def load_guide():
    with open(GUIDE_PATH, "r") as f:
        return json.load(f)


# noinspection PyTypeChecker
def analyze_aoe(casts_df: pd.DataFrame, buffs_df: pd.DataFrame, damage_df: pd.DataFrame) -> List[Dict]:
    guide = load_guide()
    important = set(guide.get("important_buffs", []))
    bursts: List[Dict] = []

    sr = casts_df.sort_values("timestamp")
    for _, row in sr.iterrows():
        if row["spell"] == "Arcane Surge":
            start = row["timestamp"]
            end = start + 8000  #

            dmg = int(damage_df.loc[
                (damage_df["timestamp"].between(start, end)) &
                (damage_df["spell"] == "Arcane Surge"),
                "dps"
            ].sum())

            buffs_window = buffs_df.loc[
                buffs_df["timestamp"].between(start, end) &
                buffs_df["buff"].isin(important)
            ]
            buffs_list = buffs_window["buff"].tolist()
            buff_counts = buffs_window["buff"].value_counts().to_dict()

            barrage_casts = int(casts_df.loc[
                (casts_df["timestamp"].between(start, end)) &
                (casts_df["spell"] == "Arcane Barrage"),
                "spell"
            ].count())

            bursts.append({
	            "start": start,
	            "end": end,
	            "damage": dmg,
	            "barrage_count": buff_counts,
	            "type": "aoe"
            })

    return bursts


