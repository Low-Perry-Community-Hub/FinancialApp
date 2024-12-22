import requests

def fetch_crypto_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {"symbol": symbol, "price": float(data["price"])}
    else:
        return {"error": "Failed to fetch price"}

def interact_with_llm(question):
    if "portfolio" in question.lower():
        # Example: Fetch and calculate portfolio value
        portfolio = query_user_portfolio("user_id_123")
        total_value = sum([item['value_usd'] for item in portfolio])
        return f"Your total portfolio value is ${total_value:.2f}"
    elif "Bitcoin" in question:
        data = query_crypto_prices("Bitcoin")
    else:
        return "I can currently help with portfolio and crypto queries."

    analysis_prompt = f"The following data was retrieved: {data}. Provide a summary."
    return ask_llm(analysis_prompt)

