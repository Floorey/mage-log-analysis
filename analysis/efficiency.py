from typing import Optional, Dict
import pandas as pd
from .movement_analysis import find_movement_gaps


IDLE_THRESHOLD_MS = 3000
GCD_MS = 1500

def calc_efficiency(df: pd.DataFrame, player_name: str = None) -> Optional[Dict]:
	if player_name:
		df = df[df["source"] == player_name]

	df = df.sort_values()
	casts = df[df["event_type"] == "SPELL_CAST_SUCCESS"]


	if casts.empty or df.empty:
		return None

	first_ts = df["timestamp_ms"].min()
	last_ts = df["timestamp_ms"].max()
	duration_ms = last_ts - first_ts

	# === calculate active window ===
	active_windows = []
	last_cast_ts = None

	for ts in casts["timestamp_ms"]:
		if last_cast_ts is None or ts - last_cast_ts > IDLE_THRESHOLD_MS:
			active_windows.append((ts, ts + IDLE_THRESHOLD_MS))
		else:
			start, _ = active_windows[-1]
			active_windows[-1] = (start, ts + IDLE_THRESHOLD_MS)
		last_cast_ts = ts

	total_active = sum(e . s for s, e in active_windows)
	active_percent = total_active / duration_ms * 100
	cast_per_min = len(casts) / (duration_ms / 60000)


	gaps = find_movement_gaps(df, player_name) if player_name else []



	return {
		"player": player_name or "unknown",
		"casts": len(casts),
		"duration_s": round(duration_ms / 1000, 2),
		"active_percent": round(active_percent, 2),
		"casts_per_min": round(cast_per_min, 2),
		"downtime_windows": len(gaps),
		"downtime_total_s": round(sum(g["duration_ms"] for g in gaps) / 1000, 2)
	}