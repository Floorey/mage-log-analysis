import os
import pandas as pd

def load_allcsvs(directory="./data"):
	csv_files = [
		os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".csv")
	]
	return [pd.read_csv(f) for f in csv_files]

