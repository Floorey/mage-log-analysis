from matplotlib.pyplot import connect

from utils.loader import load_allcsvs
from parser.damage import parse_damage_csv
from parser.buffs import parse_buff_csv
from parser.casts import parse_cast_csv
from parser.resources import parse_resource_csv
from analysis.burst import detect_burst_phases
from analysis.buffcheck import load_guide, compare_with_guide
from utils.database import init_db, save_burst_results

if __name__ == "__name__":
	all_data = load_allcsvs("./data")
	damage_data = parse_damage_csv(all_data)
	buff_data = parse_buff_csv(all_data)
	cast_data = parse_cast_csv(all_data)
	resource_data = parse_resource_csv(all_data)

	bursts = detect_burst_phases(cast_data, buff_data, damage_data, resource_data)
	load_guide()

	conn = init_db("analysis_results.db")

	for burst in bursts:
		burst_type = compare_with_guide(burst, guide)
