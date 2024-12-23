from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ...core.database import get_db
from ...services.portfolio_service import PortfolioService
from ...models.portfolio import Portfolio, PortfolioAsset

router = APIRouter()

@router.post("/portfolio/", response_model=Portfolio)
async def create_portfolio(user_id: str, name: str, db: Session = Depends(get_db)):
    portfolio_service = PortfolioService(db)
    return portfolio_service.create_portfolio(user_id, name)

@router.post("/portfolio/{portfolio_id}/asset", response_model=PortfolioAsset)
async def add_asset(
    portfolio_id: int,
    asset_name: str,
    quantity: float,
    purchase_price: float,
    db: Session = Depends(get_db)
):
    portfolio_service = PortfolioService(db)
    return portfolio_service.add_asset(portfolio_id, asset_name, quantity, purchase_price)

@router.get("/portfolio/{portfolio_id}", response_model=Portfolio)
async def get_portfolio(portfolio_id: int, db: Session = Depends(get_db)):
    portfolio_service = PortfolioService(db)
    portfolio = portfolio_service.get_portfolio(portfolio_id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio