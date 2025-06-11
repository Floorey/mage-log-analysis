def parse_buff_csv(csv_list):
	all_buffs = []
	for df in csv_list:
		if 'event_type' in df.columns and 'buff' in df.columns:
			buff_rows = df[df['event_type'].isin(['applybuff', 'refreshbuff'])]
			for _, row in buff_rows.iterrows():
				all_buffs.append({
					"timestamp": int(row['timestamp']),
					"name": row['buf']
				})
	return all_buffs

