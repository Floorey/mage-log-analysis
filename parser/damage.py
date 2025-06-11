import pandas as pd


def parse_damage_csv(all_dfs):
    damages = []
    for df in all_dfs:
        if "timestamp" in df.columns and "spell" in df.columns and "damage" in df.columns:
            filtered = df[["timestamp", "spell", "damage"]].dropna()
            for _, row in filtered.iterrows():
                try:
                    ts = int(row["timestamp"])
                    dmg = int(row["damage"])
                    spell = str(row["spell"])
                except (ValueError, TypeError):
                    continue
                damages.append({"timestamp": ts, "spell": spell, "dps": dmg, "source_name": row.get("source_name")})
    return pd.DataFrame(damages)
