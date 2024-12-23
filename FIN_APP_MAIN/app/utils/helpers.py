from fastapi import HTTPException
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

class AppError(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

def handle_error(error: Exception) -> Dict[str, Any]:
    logger.error(f"Error occurred: {str(error)}")
    if isinstance(error, AppError):
        raise HTTPException(status_code=error.status_code, detail=error.message)
    raise HTTPException(status_code=500, detail="Internal server error")