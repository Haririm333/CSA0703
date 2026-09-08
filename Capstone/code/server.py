"""
Module 2 — Centralized Control Program (Server side)

Central control server for the Smart Street Light Control Network.

Responsibilities:
  1. Accept TCP connections from the 5 simulated street-light controller
     nodes (Module 1's network topology, represented here as socket clients).
  2. Run a 24-hour lighting schedule (time-compressed for demo purposes)
     and broadcast ON/OFF commands to every connected node at the correct
     simulated hour.
  3. Log every command sent (timestamp, node, command, delivery result) to
     a CSV file that stands in for a Wireshark packet capture — this file
     is consumed by verify_report.py (Module 3).
"""

import socket
import threading
import time
import json
import csv
import os
from datetime import datetime

import config


class ControlServer:
    def __init__(self):
        self.clients = {}          # node_id -> socket
        self.clients_lock = threading.Lock()
        self.running = True

        os.makedirs(config.LOG_DIR, exist_ok=True)
        self._init_command_log()

    def _init_command_log(self):
        with open(config.COMMAND_LOG, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["real_timestamp", "sim_hour", "node_id", "command", "delivery_status"]
            )

    def _log_command(self, sim_hour, node_id, command, status):
        with open(config.COMMAND_LOG, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [datetime.now().isoformat(timespec="seconds"), sim_hour, node_id, command, status]
            )

    def start(self):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((config.HOST, config.PORT))
        server_sock.listen(config.NUM_NODES)
        print(f"[SERVER] Listening on {config.HOST}:{config.PORT}")

        accept_thread = threading.Thread(target=self._accept_loop, args=(server_sock,), daemon=True)
        accept_thread.start()

        # Wait until all nodes have registered before starting the schedule
        print(f"[SERVER] Waiting for {config.NUM_NODES} nodes to connect...")
        while len(self.clients) < config.NUM_NODES:
            time.sleep(0.2)
        print(f"[SERVER] All {config.NUM_NODES} nodes connected. Starting schedule.\n")

        self._run_schedule()

        self.running = False
        server_sock.close()
        print("[SERVER] Schedule complete. Server shutting down.")

    def _accept_loop(self, server_sock):
        while self.running:
            try:
                server_sock.settimeout(1.0)
                conn, addr = server_sock.accept()
            except socket.timeout:
                continue
            except OSError:
                break

            try:
                register_msg = json.loads(conn.recv(1024).decode())
                node_id = register_msg["node_id"]
                with self.clients_lock:
                    self.clients[node_id] = conn
                print(f"[SERVER] Registered {node_id} from {addr}")
            except Exception as e:
                print(f"[SERVER] Failed to register client {addr}: {e}")

    def _broadcast(self, sim_hour, command):
        with self.clients_lock:
            for node_id, conn in self.clients.items():
                payload = json.dumps(
                    {"cmd": command, "sim_hour": sim_hour, "sent_at": datetime.now().isoformat()}
                ) + "\n"
                try:
                    conn.sendall(payload.encode())
                    status = "DELIVERED"
                except Exception:
                    status = "FAILED"
                self._log_command(sim_hour, node_id, command, status)
        print(f"[SERVER] Hour {sim_hour:02d}:00 -> broadcast '{command}' to {len(self.clients)} nodes")

    def _run_schedule(self):
        for sim_hour in range(config.SIM_HOURS_PER_DAY):
            if sim_hour in config.SCHEDULE:
                self._broadcast(sim_hour, config.SCHEDULE[sim_hour])
            time.sleep(config.SECONDS_PER_SIM_HOUR)

        # Send a final SHUTDOWN so node clients can exit cleanly
        with self.clients_lock:
            for node_id, conn in self.clients.items():
                try:
                    conn.sendall((json.dumps({"cmd": "SHUTDOWN"}) + "\n").encode())
                except Exception:
                    pass


if __name__ == "__main__":
    ControlServer().start()
