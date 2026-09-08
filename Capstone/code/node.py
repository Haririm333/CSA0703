"""
Module 1 — Street Light Node Network Design (Runtime side)

Simulates a single street-light controller node. In the Packet Tracer
topology this is one of the 5 IoT devices; here it is a lightweight TCP
client that:
  1. Registers itself with the central control server.
  2. Listens for ON/OFF commands.
  3. Maintains and logs its own state history (used later to cross-check
     the server's command log during verification).

Usage:
    python node.py NODE-01
"""

import socket
import json
import sys
import csv
import os
from datetime import datetime

import config


class StreetLightNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.state = "OFF"  # default state before first command
        os.makedirs(config.LOG_DIR, exist_ok=True)
        self.log_path = config.NODE_LOG_TEMPLATE.format(node_id=node_id)
        self._init_log()

    def _init_log(self):
        with open(self.log_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["real_timestamp", "sim_hour", "state"])

    def _log_state(self, sim_hour, state):
        with open(self.log_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().isoformat(timespec="seconds"), sim_hour, state])

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((config.HOST, config.PORT))
        sock.sendall(json.dumps({"node_id": self.node_id}).encode())
        print(f"[{self.node_id}] Connected and registered.")

        buffer = ""
        while True:
            data = sock.recv(1024).decode()
            if not data:
                break
            buffer += data
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                if not line.strip():
                    continue
                msg = json.loads(line)
                if msg["cmd"] == "SHUTDOWN":
                    print(f"[{self.node_id}] Received shutdown signal. Exiting.")
                    sock.close()
                    return
                self.state = msg["cmd"]
                sim_hour = msg.get("sim_hour", -1)
                self._log_state(sim_hour, self.state)
                print(f"[{self.node_id}] Hour {sim_hour:02d}:00 -> state changed to {self.state}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python node.py <NODE_ID>")
        sys.exit(1)
    StreetLightNode(sys.argv[1]).run()
