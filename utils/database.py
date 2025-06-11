import sqlite3
import json


def init_db(path="analysis_result.db"):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bursts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            burst_type TEXT,
            damage INTEGER,
            buffs TEXT,
            spells TEXT,
            resources TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_burst_to_db(path: str, burst: dict, burst_type: str):
    conn =sqlite3.connect(path)
    c = conn.cursor()
    c.e




    