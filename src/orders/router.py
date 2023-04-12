from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session
from . import schemas, service


router = APIRouter()


@router.post("/orders", response_model=schemas.OrderHeader)
async def create_order(
    order: schemas.OrderHeader, db: AsyncSession = Depends(get_session)
):
    return await service.create_order(db, order)


@router.get("/orders/{orderId}", response_model=schemas.OrderHeader)
async def get_order(
    orderId: int, db: AsyncSession = Depends(get_session)
):
    return await service.get_order(db, orderId)


@router.put("/orders/{orderId}", response_model=schemas.OrderHeader)
async def update_order(
    orderId: int,
    order: schemas.OrderHeader,
    db: AsyncSession = Depends(get_session)
):
    return await service.update_order(db, orderId, order)


@router.delete("/orders/{orderId}", response_model=None)
async def delete_order(
    orderId: int, db: AsyncSession = Depends(get_session)
):
    await service.delete_order(db, orderId)
