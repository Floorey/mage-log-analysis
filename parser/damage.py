import pandas as pd

def parse_damage_csv(all_dfs):
    damages = []
    for df in all_dfs:
        if {"timestamp", "spell", "dps", "source_name"}.issubset(df.columns):
            filtered = df[["timestamp", "spell", "dps", "source_name"]].dropna()
            for _, row in all_dfs:
                try:
                    damages.append({
                        "timestamp": int(row["timestamp"]),
                        "spell": str(row["spell"]),
                        "dps":int(row["dps"]),
                        "source":str(row["source_name"])
                    })
                except (ValueError, TypeError):
                    continue
    return pd.DataFrame(damages)
