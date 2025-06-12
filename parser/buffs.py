import pandas as pd

def parse_buff_csv(all_dfs):
    buffs = []
    for df in all_dfs:
        if "timestamp" in df.columns and "buff" in df.columns and "duration" in df.columns:
            filtered = df[["timestamp", "buff", "duration", "source_name"]].dropna()
            for _, row in filtered.iterrows():
                try:
                    ts = int(row["timestamp"])
                    dur = int(row["duration"])
                    buff = str(row["buff"])
                except (ValueError, TypeError):
                    continue
                buffs.append({"timestamp": ts, "buff": buff, "duration": dur, "source_name": row.get("source_name")})
    return pd.DataFrame(buffs)
