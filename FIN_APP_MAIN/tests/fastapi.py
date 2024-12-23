from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import uvicorn

app = FastAPI(title="Crypto Tracking API")

@app.get("/test/{crypto_name}")
async def test_crypto_price(crypto_name: str):
    try:
        # Test request
        url = "https://api.tiingo.com/tiingo/crypto/prices"
        params = {
            'tickers': f"{crypto_name.lower()}usd",
            'startDate': '2019-01-02',
            'resampleFreq': '5min',
            'token': 'dd6b9a02929cbbd332fdd37d8ef3990c7ef6feb3'
        }
        
        response = requests.get(url, params=params)
        
        return {
            "status": response.status_code,
            "url": response.url,
            "response": response.json(),
            "headers": dict(response.headers)
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "type": str(type(e))
        }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)