from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
import requests
import uvicorn
from datetime import datetime

app = FastAPI(title="Financial Portfolio API")

TIINGO_API_KEY = "dd6b9a02929cbbd332fdd37d8ef3990c7ef6feb3"

class Asset(BaseModel):
    symbol: str
    quantity: float
    asset_type: str  # 'stock' or 'crypto'

portfolio: List[Dict] = []

def get_stock_price(symbol: str) -> float:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {TIINGO_API_KEY}'
    }
    
    try:
        # Using Tiingo's IEX endpoint for real-time stock prices
        url = f"https://api.tiingo.com/iex/{symbol}"
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if data and len(data) > 0:
            return float(data[0]['last'])
        raise HTTPException(status_code=404, detail=f"Stock {symbol} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_crypto_price(symbol: str) -> float:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {TIINGO_API_KEY}'
    }
    
    try:
        # Using Tiingo's crypto endpoint
        url = f"https://api.tiingo.com/tiingo/crypto/prices"
        params = {
            'tickers': f"{symbol.lower()}usd",
            'resampleFreq': '1min'
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        
        if data and len(data) > 0:
            return float(data[0]['close'])
        raise HTTPException(status_code=404, detail=f"Crypto {symbol} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {
        "message": "Financial Portfolio API",
        "version": "1.0",
        "endpoints": [
            "/price/stock/{symbol}",
            "/price/crypto/{symbol}",
            "/portfolio"
        ]
    }

@app.get("/price/stock/{symbol}")
async def get_stock_price_endpoint(symbol: str):
    try:
        price = get_stock_price(symbol.upper())
        return {
            "status": "success",
            "data": {
                "symbol": symbol.upper(),
                "price": price,
                "currency": "USD",
                "timestamp": datetime.now().isoformat()
            }
        }
    except HTTPException as e:
        return {
            "status": "error",
            "error": str(e.detail),
            "symbol": symbol
        }

@app.get("/price/crypto/{symbol}")
async def get_crypto_price_endpoint(symbol: str):
    try:
        price = get_crypto_price(symbol.upper())
        return {
            "status": "success",
            "data": {
                "symbol": symbol.upper(),
                "price": price,
                "currency": "USD",
                "timestamp": datetime.now().isoformat()
            }
        }
    except HTTPException as e:
        return {
            "status": "error",
            "error": str(e.detail),
            "symbol": symbol
        }

@app.post("/portfolio")
async def add_to_portfolio(asset: Asset):
    try:
        # Get current price based on asset type
        if asset.asset_type.lower() == 'stock':
                        current_price = get_stock_price(asset.symbol)
        elif asset.asset_type.lower() == 'crypto':
            current_price = get_crypto_price(asset.symbol)
        else:
            raise HTTPException(status_code=400, detail="Invalid asset type. Must be 'stock' or 'crypto'")
        
        portfolio_item = {
            "symbol": asset.symbol.upper(),
            "asset_type": asset.asset_type.lower(),
            "quantity": float(asset.quantity),
            "current_price": current_price,
            "total_value": current_price * float(asset.quantity),
            "added_at": datetime.now().isoformat()
        }
        
        portfolio.append(portfolio_item)
        return {
            "status": "success",
            "data": portfolio_item
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "symbol": asset.symbol
        }

@app.get("/portfolio")
async def get_portfolio():
    try:
        updated_portfolio = []
        total_value = 0.0
        
        for item in portfolio:
            try:
                if item['asset_type'] == 'stock':
                    current_price = get_stock_price(item['symbol'])
                else:
                    current_price = get_crypto_price(item['symbol'])
                    
                updated_item = item.copy()
                updated_item['current_price'] = current_price
                updated_item['total_value'] = current_price * item['quantity']
                total_value += updated_item['total_value']
                updated_portfolio.append(updated_item)
            except:
                updated_portfolio.append(item)
        
        return {
            "status": "success",
            "data": {
                "portfolio": updated_portfolio,
                "total_portfolio_value": total_value,
                "last_updated": datetime.now().isoformat()
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

@app.delete("/portfolio/{symbol}")
async def delete_from_portfolio(symbol: str):
    try:
        original_length = len(portfolio)
        portfolio[:] = [item for item in portfolio if item['symbol'] != symbol.upper()]
        
        if len(portfolio) == original_length:
            raise HTTPException(status_code=404, detail=f"Asset {symbol} not found in portfolio")
            
        return {
            "status": "success",
            "message": f"Removed {symbol.upper()} from portfolio"
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)