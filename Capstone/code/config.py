"""
Shared configuration for the Smart Street Light Control Network simulation.

Time compression: to demo a full 24-hour schedule quickly, we compress
1 simulated hour into SECONDS_PER_SIM_HOUR real seconds. Change this to 3600
to run the system in true real-time.
"""

HOST = "127.0.0.1"
PORT = 5050

NUM_NODES = 5
NODE_IDS = [f"NODE-{i+1:02d}" for i in range(NUM_NODES)]

# --- Time compression for demo purposes ---
SECONDS_PER_SIM_HOUR = 1.5   # 24 sim-hours run in 36 real seconds
SIM_HOURS_PER_DAY = 24

# --- Municipal lighting schedule (24-hour clock, simulated hours) ---
# Lights should be ON only during non-daylight hours.
SCHEDULE = {
    6: "OFF",   # sunrise -> switch off
    18: "ON",   # sunset  -> switch on
}

LOG_DIR = "logs"
COMMAND_LOG = f"{LOG_DIR}/command_log.csv"
NODE_LOG_TEMPLATE = f"{LOG_DIR}/node_{{node_id}}_log.csv"
