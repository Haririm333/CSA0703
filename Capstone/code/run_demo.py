"""
Demo runner — launches the central server and all 5 street-light nodes as
subprocesses, lets a full simulated 24-hour schedule play out, then
automatically runs the Module 3 verification report.

This is what you run for a live demo during the capstone review:

    python run_demo.py
"""

import subprocess
import sys
import time

import config


def main():
    print("=" * 60)
    print("SMART STREET LIGHT CONTROL NETWORK — LIVE DEMO")
    print(f"Simulated 24-hour cycle, {config.SECONDS_PER_SIM_HOUR}s per sim-hour")
    print("=" * 60, "\n")

    server_proc = subprocess.Popen([sys.executable, "server.py"])
    time.sleep(1.5)  # let the server bind/listen before nodes connect

    node_procs = []
    for node_id in config.NODE_IDS:
        p = subprocess.Popen([sys.executable, "node.py", node_id])
        node_procs.append(p)
        time.sleep(0.3)

    server_proc.wait()
    for p in node_procs:
        p.wait(timeout=10)

    print("\n[DEMO] All processes finished. Generating verification report...\n")
    subprocess.run([sys.executable, "verify_report.py"])


if __name__ == "__main__":
    main()
