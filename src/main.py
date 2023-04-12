from fastapi import FastAPI

from src.customers.router import router as customers_router
from src.products.router import router as products_router


app = FastAPI()
app.include_router(customers_router)
app.include_router(products_router)
