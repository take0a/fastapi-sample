from fastapi import FastAPI

from src.customers.router import router as customers_router

app = FastAPI()
app.include_router(customers_router)
