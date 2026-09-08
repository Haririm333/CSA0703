"""
Module 3 — Energy-Saving Verification Report

In the real deployment this reads a Wireshark capture (.pcap / exported CSV)
of the command traffic between the control server and the light nodes. In
this simulation, command_log.csv (written by server.py) plays that role —
it has the same information a filtered Wireshark capture would give you:
timestamp, source/destination (node_id), and the command payload (ON/OFF).

It calculates, per node and for the network overall:
  - total scheduled OFF duration (hours the light was off during the day)
  - estimated % of electricity saved vs. a "lights always on" baseline
  - command delivery success rate (from the DELIVERED/FAILED status)
"""

import csv
from collections import defaultdict

import config


def load_command_log():
    rows = []
    with open(config.COMMAND_LOG, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["sim_hour"] = int(row["sim_hour"])
            rows.append(row)
    return rows


def compute_off_hours(rows):
    """
    For each node, walk through its ON/OFF events in simulated-hour order
    and sum up the hours spent in the OFF state across the 24-hour cycle.
    """
    events_by_node = defaultdict(list)
    for row in rows:
        events_by_node[row["node_id"]].append((row["sim_hour"], row["command"]))

    off_hours_by_node = {}
    for node_id, events in events_by_node.items():
        events.sort(key=lambda e: e[0])
        off_hours = 0
        # Assume state holds from one event until the next; cycle wraps at 24h.
        for i, (hour, cmd) in enumerate(events):
            next_hour = events[i + 1][0] if i + 1 < len(events) else events[0][0] + config.SIM_HOURS_PER_DAY
            duration = next_hour - hour
            if cmd == "OFF":
                off_hours += duration
        off_hours_by_node[node_id] = off_hours
    return off_hours_by_node


def compute_delivery_rate(rows):
    total = len(rows)
    delivered = sum(1 for r in rows if r["delivery_status"] == "DELIVERED")
    return (delivered / total * 100) if total else 0.0


def generate_report():
    rows = load_command_log()
    off_hours_by_node = compute_off_hours(rows)
    delivery_rate = compute_delivery_rate(rows)

    lines = []
    lines.append("=" * 60)
    lines.append("ENERGY-SAVING VERIFICATION REPORT")
    lines.append("Smart Street Light Control Network — Capstone Review 1")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"{'Node ID':<12}{'OFF Hours / 24h':<20}{'Est. Energy Saved':<20}")
    lines.append("-" * 52)

    total_off = 0
    for node_id in sorted(off_hours_by_node):
        off_hours = off_hours_by_node[node_id]
        saved_pct = (off_hours / config.SIM_HOURS_PER_DAY) * 100
        total_off += off_hours
        lines.append(f"{node_id:<12}{off_hours:<20}{saved_pct:.1f}%")

    avg_saved_pct = (total_off / (len(off_hours_by_node) * config.SIM_HOURS_PER_DAY)) * 100

    lines.append("-" * 52)
    lines.append(f"\nNetwork-wide average energy saved: {avg_saved_pct:.1f}%")
    lines.append(f"Command delivery success rate:     {delivery_rate:.1f}%")
    lines.append(f"Total commands captured:            {len(rows)}")
    lines.append("")
    lines.append(
        "Interpretation: lights were automatically switched OFF during "
        f"daylight hours (06:00-18:00), saving power for ~{avg_saved_pct:.0f}% "
        "of the day compared to a baseline where lights stay on 24/7."
    )
    lines.append("=" * 60)

    report_text = "\n".join(lines)
    print(report_text)

    with open("reports/energy_report.txt", "w") as f:
        f.write(report_text)
    print("\n[REPORT] Saved to reports/energy_report.txt")


if __name__ == "__main__":
    import os
    os.makedirs("reports", exist_ok=True)
    generate_report()
