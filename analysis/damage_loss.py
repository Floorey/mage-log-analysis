from database_efficiency.analysis_storage import store_damage_loss


def estimate_dps_loss(efficiency: dict, total_damage: float) -> dict:
    """
    Schätzt den DPS-Verlust durch Downtime anhand Effizienz-Metriken.

    Args:
        efficiency (dict): Ergebnis von calc_efficiency()
        total_damage (float): Tatsächlich verursachter Schaden im Kampf.

    Returns:
        dict: DPS-Verlust, theoretischer DPS, verlorener Schaden etc.
    """
    if not efficiency or efficiency["duration_s"] == 0:
        return {}

    real_dps = total_damage / efficiency["duration_s"]
    active_time_s = efficiency["duration_s"] - efficiency["downtime_total_s"]
    ideal_dps = total_damage / active_time_s if active_time_s > 0 else real_dps

    lost_damage = ideal_dps * efficiency["downtime_total_s"]
    dps_loss_percent = lost_damage / total_damage * 100 if total_damage > 0 else 0

    store_damage_loss("player_name", 120000, 95000, 20.8)

    return {
        "real_dps": round(real_dps, 2),
        "ideal_dps": round(ideal_dps, 2),
        "lost_damage": round(lost_damage, 2),
        "lost_dps_percent": round(dps_loss_percent, 2),
        "downtime_s": round(efficiency["downtime_total_s"], 2),
    }

