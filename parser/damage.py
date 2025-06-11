from fontTools.ttLib.tables.otTraverse import dfs_base_table


def parse_damage_csv(csv_list):
	all_damage = []
	for df in csv_list:
		if 'event_type' in df.columns and 'damage' in df.columns:
			damage_rows =df[df['event_type'] == 'damage']
			for _, row in damage_rows.iterrows():
				all_damage.append({
					"timestamp": int(row['timestamp']),
					"spell": row['spell'],
					"amount": int(row['damage'])
				})
	return all_damage