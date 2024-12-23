from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.portfolio import Portfolio, PortfolioAsset
from ..utils.helpers import AppError

class PortfolioService:
    def __init__(self, db: Session):
        self.db = db

    def create_portfolio(self, user_id: str, name: str) -> Portfolio:
        portfolio = Portfolio(user_id=user_id, name=name)
        self.db.add(portfolio)
        self.db.commit()
        self.db.refresh(portfolio)
        return portfolio

    def add_asset(self, portfolio_id: int, asset_name: str, quantity: float, purchase_price: float) -> PortfolioAsset:
        portfolio = self.db.query(Portfolio).filter(Portfolio.id == portfolio_id).first()
        if not portfolio:
            raise AppError("Portfolio not found", 404)
        
        asset = PortfolioAsset(
            portfolio_id=portfolio_id,
            asset_name=asset_name,
            quantity=quantity,
            purchase_price=purchase_price
        )
        self.db.add(asset)
        self.db.commit()
        self.db.refresh(asset)
        return asset

    def get_portfolio(self, portfolio_id: int) -> Optional[Portfolio]:
        return self.db.query(Portfolio).filter(Portfolio.id == portfolio_id).first()