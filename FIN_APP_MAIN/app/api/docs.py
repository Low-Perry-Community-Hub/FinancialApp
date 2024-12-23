from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FinancialApp API",
        version="1.0.0",
        description="A modern cryptocurrency and portfolio tracking application",