def parse_cast_csv(csv_list):
	all_casts = []
	for df in csv_list:
		if 'event_type' in df.columns and 'spell' in df.columns:
			cast_rows = df[df['event_type'] == 'cast']
			for _, row in cast_rows.iterrows():
				all_casts.append({
					"timestamp": int(row['timestamp']),
					"mana": row['spell']
				})
	return all_casts