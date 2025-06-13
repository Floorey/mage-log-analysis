import pandas as pd
from datetime import datetime



def parse_combatlog(file_path: str) -> pd.DataFrame:
	"""
	Parses the WoW CombatLog.txt into data frame
	 Args:
	        file_path (str): path CombatLog.txt.

	    Returns:
	        pd.DataFrame: table for Timestamp, Eventtyp, Source, Spell etc.

	"""

	rows = []

	with open(file_path, "r", encoding="utf-8") as f:
		for line in f:
			parts = line.strip().split(",")
			if len(parts) < 4 or not parts[0][0].isdigit():
				continue

			try:
				datetime_str = parts[0]
				time_part =parts[1]
				event_type = parts[2].strip()
				ts = datetime.strptime(f"{datetime_str} {time_part}", "%m/%d %H:%M:%S.%f")
				source = parts[3].strip()
				spell = parts[5].strip() if len(parts) > 5 else None
			except Exception:
				continue

			rows.append({
				"timestamp": ts,
				"event_type": event_type,
				"source": source,
				"spell": spell
			})

	df = pd.DataFrame(rows)
	df["timestamp_ms"] = df["timestamp"].astype("int64") // 1_000_000
	return df
