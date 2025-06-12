import json
import pandas as pd
from typing import List, Dict

from pandas import DataFrame

GUIDE_PATH = "guide/arcane_burst_guide_st.json"


def load_guide() -> Dict:
	with open(GUIDE_PATH, "r") as f:
		return json.load(f)


# noinspection PyTypeChecker
def analyze_single_target(
		casts_df: pd.DataFrame,
		buffs_df: pd.DataFrame,
		damage_df: pd.DataFrame
) -> None:
	"""

	:param damage_df:
	:param buffs_df:
	:type casts_df: pd.DataFrame
	"""
	guide = load_guide()
	important = set(guide.get("important_buffs", []))
	bursts: List[Dict] = []
	
	sr = casts_df.sort_values("timestamp")
	for _, row in sr.iterrows():
		if row["spell"] == "Arcane Surge":
			start = row["timestamp"]
			end = start + 15000
			
			dmg_series = damage_df.loc[
				(damage_df["timestamp"].between(start, end)) &
				(damage_df["spell"] == "Arcane Surge"),
				"dps"
			]
			damage = int(dmg_series.sum()) if not dmg_series.empty else 0

			buffs_window = buffs_df.loc[
				buffs_df["timestamp"].between(start, end) &
				buffs_df["spell"].isin(important),
				"buff"
			]
			buff_counts = buffs_window.value_counts().to_dict()
			buffs_list = list(buff_counts.keys())

			# noinspection PyTypeChecker
			barrage_casts = int(
				casts_df.loc[
					(casts_df["timestamp"].between(start, end)) &
					(casts_df["spell"] == "Arcane Barrage"),
					"spell"
				].count()

			)
			bursts.append(dict(start=start, end=end, damage=damage, barrage_count=barrage_casts, buffs=buffs_list,
			                   buff_uptime=buff_counts, type="single_target"))

	return bursts
