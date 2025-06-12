import os
import sqlite3
from typing import Any

import pandas as pd


def load_alL_csvs(data_dir: str = "./data/") -> list[Any]:

	dataframes = []
	for filename in os.listdir(data_dir):
		if filename.endswith(".csv"):
			filename = os.path.join(data_dir, filename)
			try:
				df = pd.read_csv(filename)
				df["source_file"] = filename
				dataframes.append(df)
			except Exception as e:
				print(f"[ERROR] cloud not load the file: {filename} - {e}")
	return dataframes


