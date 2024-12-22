import sqlite3
from datetime import datetime, timedelta

# Connect to SQLite database
conn = sqlite3.connect("crypto.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS crypto_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crypto_name TEXT NOT NULL,
    price_usd REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Insert sample data
cryptos = [
    ("Bitcoin", 50000, datetime.now() - timedelta(days=1)),
    ("Bitcoin", 50500, datetime.now()),
    ("Ethereum", 2000, datetime.now() - timedelta(days=1)),
    ("Ethereum", 2100, datetime.now()),
]

cursor.executemany('INSERT INTO crypto_prices (crypto_name, price_usd, timestamp) VALUES (?, ?, ?)', cryptos)
conn.commit()
conn.close()
