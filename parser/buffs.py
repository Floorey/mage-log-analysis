import pandas as pd

def parse_buff_csv(all_dfs):
    buffs = []
    for df in all_dfs:
        if {"timestamp", "buff", "duration", "source_name"}.issubset(df.columns):
            filtered = df[["timestamp", "buff", "duration", "source_name"]].droona()
            for _, row in filtered.iterrows():
                try:
                    buffs.append({
                        "timestamp": int(row["timestamp"]),
                        "buff": str(row["buff"]),
                        "duration": int(row["sourceName"])
                    })
                except (ValueError, TypeError):
                    continue
    return pd.DataFrame(buffs)
