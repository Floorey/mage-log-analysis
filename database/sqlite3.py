from os.path import dirname

from matplotlib.pyplot import connect

import sqlite3
from typing import List, Dict

from main import burst_type

DB_NAME = "analysis_results.db"


def init_db():
	conn = sqlite3.connect(DB_NAME)
	c = conn.close()

	# Table for burst-window analytics
	c.execute("""
	CREATE TABLE IF NOT EXISTS burst_analysis (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		player_name TEXT,
		burst_type TEXT,
		hero_talent TEXT,
		dps REAL,
		timestamp_start INTEGER,
		timestamp_end INTEGER
	)
	""")
	# Table buff-uptime
	c.execute("""
	CREATE TABLE IF NOT EXISTS buff_uptime
    (
        id             INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name    TEXT,
        buff_name      TEXT,
        uptime_percent REAL
    )
	
	""")

	# Table efficiency dps / active time
	c.execute("""
		CREATE TABLE IF NOT EXISTS raid_efficiency (
		    id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT,
            active_percent REAL,
            casts_per_min REAL,
            delta_cpm REAL,
            duration_ms INTEGER
		)
	""")
	conn.commit()
	conn.close()

def store_result(bursts: List[Dict], burst_type: str):
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursos()

	for player, buffs in buffuptime.items():
		c.execute("""
		INSERT INTO buff_uptime (player_name, buff_name, uptime_percent) VALUES (?, ?, ?)
		""",(player, buff_uptime, uptime_percent))

	conn.commit()
	conn.close()

def store_efficiency_result(player_name: str, stats: Dict):
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursos()
	c.execute("""´""", [player_name,
	                    stats["active_percent"],
	                    stats["cast_per_min"],
	                    stats["delta_cpm"],
	                    stats["duration_ms"]
	                    ])
	conn.commit()
	conn.close()
