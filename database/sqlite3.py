import sqlite3
import json

DB_PATH = "mage_analysis.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS bursts (
        id INTEGER PRIMARY KEY,
        burst_type TEXT,
        start INTEGER,
        end INTEGER,
        damage INTEGER,
        barrage_count INTEGER,
        buffs TEXT,
        buff_uptime TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS casts (
        id INTEGER PRIMARY KEY,
        timestamp INTEGER,
        spell TEXT,
        source TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS buffs (
        id INTEGER PRIMARY KEY,
        timestamp INTEGER,
        buff TEXT,
        duration INTEGER,
        source TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS damage (
        id INTEGER PRIMARY KEY,
        timestamp INTEGER,
        spell TEXT,
        dps INTEGER,
        source TEXT
    )""")
    conn.commit()
    conn.close()

def insert_casts(casts):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.executemany("INSERT INTO casts (timestamp, spell, source) VALUES (:timestamp, :spell, :source)", casts)
    conn.commit()
    conn.close()

def insert_buffs(buffs):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.executemany("INSERT INTO buffs (timestamp, buff, duration, source) VALUES (:timestamp, :buff, :duration, :source)", buffs)
    conn.commit()
    conn.close()

def insert_damage(dmg_entries):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.executemany("INSERT INTO damage (timestamp, spell, dps, source) VALUES (:timestamp, :spell, :dps, :source)", dmg_entries)
    conn.commit()
    conn.close()

def insert_bursts(player, bursts):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    for b in bursts:
        c.execute("""
          
        """, (
            b["type"], b["start"], b["end"], b["damage"],
            b.get("barrage_count", 0),
            json.dumps(b.get("buffs", [])),
            json.dumps(b.get("buff_uptime", {}))
        ))
    conn.commit()
    conn.close()
