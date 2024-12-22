import sqlite3

def query_crypto_prices(crypto_name):
    conn = sqlite3.connect("crypto.db")
    cursor = conn.cursor()
    
    # Query prices for the given crypto
    cursor.execute('''
    SELECT crypto_name, price_usd, timestamp 
    FROM crypto_prices 
    WHERE crypto_name = ?
    ORDER BY timestamp DESC
    ''', (crypto_name,))
    
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    print(query_crypto_prices("Bitcoin"))
    print(query_crypto_prices("Ethereum"))
