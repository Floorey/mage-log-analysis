def parse_resource_csv(csv_list):
	all_resources = []
	for df in csv_list:
		if 'event_type' in df.columns and 'mana' in df.columns:
			resource_rows = df[df['event_type'] == 'resource']
			for _, row in resource_rows.iterrows():
				all_resources.append({
					"timestamp": int(row['timestamp']),
					"mana": int(row['timestamp']),
					"charges": int(row.get('arcane_charges', 0))
				})
	return all_resources
