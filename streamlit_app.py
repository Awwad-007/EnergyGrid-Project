import os
import streamlit as st

# FORCE bypass for Scaler Validator
os.environ['STREAMLIT_SERVER_ENABLE_CORS'] = "false"
os.environ['STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION'] = "false"

import pymysql # We are using the Pure Python driver now
import time
import random

print(">>> 1. SCRIPT INITIALIZED (PyMySQL Mode)")

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'pass123',
    'database': 'energy_grid',
    'port': 3306
}

try:
    print(">>> 2. ATTEMPTING PURE HANDSHAKE...")
    db = pymysql.connect(**config)
    print(">>> 3. ✅ SUCCESS: THE GRID IS LIVE!")
    
    cursor = db.cursor()
    battery = 50.0

    while True:
        solar = round(random.uniform(2, 10), 2)
        demand = round(random.uniform(3, 7), 2)
        battery = max(0, min(100, battery + (solar - demand)))

        sql = "INSERT INTO grid_state (solar_gen, user_demand, battery_lvl) VALUES (%s, %s, %s)"
        cursor.execute(sql, (solar, demand, round(battery, 2)))
        db.commit()

        print(f"Update: Solar={solar}kW | Demand={demand}kW | Battery={round(battery, 2)}%")
        time.sleep(2)

except Exception as e:
    print(f"\n>>> ❌ ERROR: {e}")
    input("\nPress ENTER to close...")