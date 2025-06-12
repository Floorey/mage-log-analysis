import pandas as pd

def parse_cast_csv(all_dfs):
    casts = []
    for df in all_dfs:
        if "timestamp" in df.columns and "spell" in df.columns and "event_type" in df.columns:
            filtered = df[(df["event_type"] == "cast") & df["timestamp"].notna() & df["spell"].notna()]
            for _, row in filtered.iterrows():
                try:
                    ts = int(row["timestamp"])
                    spell = str(row["spell"])
                except (ValueError, TypeError):
                    continue
                casts.append({"timestamp": ts, "spell": spell, "source_name": row.get("source_name")})
    return pd.DataFrame(casts)
urn pd.DataFrame(casts)