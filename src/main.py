import time
import logging
from fastapi import FastAPI, Request

from src.customers.router import router as customers_router
from src.products.router import router as products_router
from src.orders.router import router as orders_router


app = FastAPI()
app.include_router(customers_router)
app.include_router(products_router)
app.include_router(orders_router)

logger = logging.getLogger('uvicorn')


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"process_time = {process_time*1000} ms")
    return response
