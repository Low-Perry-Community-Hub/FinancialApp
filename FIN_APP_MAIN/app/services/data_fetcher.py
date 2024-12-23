import aiohttp
from typing import Dict, Any
from ..core.config import settings
from ..utils.helpers import AppError

class DataFetcher:
    def __init__(self):
        self.base_url = "https://api.tiingo.com/tiingo"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Token {settings.TIINGO_API_KEY}'
        }

    async def fetch_crypto_price(self, crypto_symbol: str) -> Dict[str, Any]:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            try:
                url = f"{self.base_url}/crypto/prices"
                params = {
                    'tickers': crypto_symbol,
                    'resampleFreq': '1day'
                }
                async with session.get(url, params=params) as response:
                    if response.status != 200:
                        raise AppError(f"Failed to fetch crypto price", 500)
                    data = await response.json()
                    return data[0] if data else None
            except Exception as e:
                raise AppError(f"Error fetching data: {str(e)}", 500)