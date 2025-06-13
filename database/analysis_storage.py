import sqlite3
from typing import Dict, Optional

DB_PATH = "database/identifier.sqlite"

def store_efficiency_metrics(metrics: Dict):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute ( """
                  CREATE TABLE IF NOT EXISTS efficiency (
            player TEXT,
            casts INTEGER,
            duration REAL,
            active_percent REAL,
            casts_per_min REAL
        )
    """)
    cur.execute("""
        INSERT INTO efficiency (player, casts, duration, active_percent, casts_per_min)
        VALUES (?, ?, ?, ?, ?)
    """, (
        metrics["player"],
        metrics["casts"],
        metrics["duration_s"],
        metrics["active_percent"],
        metrics["casts_per_min"]
    ))

    conn.commit()
    conn.close()

def store_movement_metrics(player: str, movement_time_ms: int, total_combat_ms: int):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS movement (
            player TEXT,
            movement_time_ms INTEGER,
            total_combat_ms INTEGER
        )
    """)
    cur.execute("""
        INSERT INTO movement (player, movement_time_ms, total_combat_ms)
        VALUES (?, ?, ?)
    """, (player, movement_time_ms, total_combat_ms))

    conn.commit()
    conn.close()

def store_damage_loss(player: str, potential_dps: float, actual_dps: float, loss_percent: float):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS damage_loss (
            player TEXT,
            potential_dps REAL,
            actual_dps REAL,
            loss_percent REAL
        )
    """)
    cur.execute("""
        INSERT INTO "damage_loss" (player, potential_dps, actual_dps, loss_percent)
        VALUES (?, ?, ?, ?)
    """, (player, potential_dps, actual_dps, loss_percent))

    conn.commit()
    conn.close()
