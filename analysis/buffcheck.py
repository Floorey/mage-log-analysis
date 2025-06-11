import json
def load_guide(path="guide/arcane_burst_guide_st.json"):
	with open(path, "r") as f:
		return json.load(f)


def compare_with_guide(burst, guide):
	for burst_type, expected_buffs in guide.items():
		active_buff_names = {b["name"] for b in burst["buffs"]}
		if set(expected_buffs).issubset(active_buff_names):
			burst["type"] = burst_type
			return burst_type
	burst["type"] = "Unknown"
	return  "Unknown"