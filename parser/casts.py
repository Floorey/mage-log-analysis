import pandas as pd

def parse_cast_csv(all_dfs):
    casts = []
    for df in all_dfs:
        if {"timestamp", "spell", "event_type", "source_name"}.issubset(df.columns):
            filtered = df[
                (df["event_type"] == "cast") &
                df[["timestamp", "spell", "source_name"]].notna().all(axis=1)
            ]
            for _, row in filtered.iterrows():
                try:
                    casts.append({
                        "timestamp": int(row["timestamp"]),
                        "spell": str(row["spell"]),
                        "source": str(row["source_name"])
                    })
                except (ValueError, TypeError):
                    continue
    return pd.DataFrame(casts)
