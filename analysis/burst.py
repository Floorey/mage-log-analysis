def detect_burst_phases(cast_data, buff_data, damage_data, resource_data):
	bursts = []
	current_burst = None


	for cast in cast_data:
		if cast['spell'] in ["Arcane Surge", "Touch of the Magi"]:
			if current_burst:
				bursts.append(current_burst)
				current_burst = {
					"start":cast["timestamp"],
					"spells": [cast],
					"buffs": [],
					"damage": 0,
					"resources": []
				}
		elif current_burst:
			current_burst["spells"].append(cast)

	if current_burst:
		bursts.append(current_burst)


	for burst in bursts:
		burst_start = burst["start"]
		burst["buffs"] = [
			buff for buff in buff_data
			if abs(buff["timestamp"] - burst_start) < 3000
	]
		burst["damage"] = sum([
			d["amount"] for d in damage_data
			if burst_start <= d["timestamp"] <= burst_start + 10000
		])

		burst["resources"] = [
			r for r in resource_data
			if burst_start <= r["timestamp"] <= burst_start + 10000
		]
	return bursts

