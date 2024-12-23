from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ...core.database import get_db
from ...services.crypto_service import CryptoService
from ...models.crypto import CryptoPrice

router = APIRouter()

@router.get("/crypto/{crypto_name}", response_model=CryptoPrice)
async def get_crypto_price(crypto_name: str, db: Session = Depends(get_db)):
    crypto_service = CryptoService(db)
    price = crypto_service.get_crypto_price(crypto_name)
    if not price:
        raise HTTPException(status_code=404, detail="Crypto price not found")
    return price

@router.post("/crypto/", response_model=CryptoPrice)
async def create_crypto_price(
    crypto_name: str, 
    price_usd: float, 
    db: Session = Depends(get_db)
):
    crypto_service = CryptoService(db)
    return crypto_service.create_crypto_price(crypto_name, price_usd)