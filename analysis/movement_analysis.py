import pandas as pd
from typing import List, Dict
from database_efficiency.analysis_storage import store_movement_metrics


IDLE_THRESHOLD_MS = 3000

def find_movement_gaps(df: pd.DataFrame, player_name: str) -> List[Dict]:



	df = df[df["source"] == player_name]
	df = df[df["event_type"] == "SPELL_CAST_SUCCESS"].sort_values("timestamp_ts")


	if df.empty:
		return []



	gaps = []
	timestamps = df["timestamp_ms"].tolist()

	for i in range(1, len(timestamps)):
		prev = timestamps[i - 1]
		curr = timestamps[i]
		gap = curr - prev
		if gap >= IDLE_THRESHOLD_MS:
			gaps.append({
				"start": prev,
				"end": curr,
				"duration_ms": gap
			})
	store_movement_metrics ( "player_name", 25000, 150000 )

	return gaps

