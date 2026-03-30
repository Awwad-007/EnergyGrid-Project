import mysql.connector

print("Testing direct connection...")
try:
    c = mysql.connector.connect(host="127.0.0.1", user="root", password="pass123")
    print("✅ SUCCESS! Python found Docker.")
    curr = c.cursor()
    curr.execute("SELECT 1")
    print("✅ DATABASE IS RESPONDING.")
except Exception as e:
    print(f"❌ FAILED: {e}")