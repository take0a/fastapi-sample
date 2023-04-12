from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session
from . import schemas, service


router = APIRouter()


@router.post("/customers", response_model=schemas.Customer)
async def create_customer(
    customer: schemas.Customer, db: AsyncSession = Depends(get_session)
):
    return await service.create_customer(db, customer)


@router.get("/customers/{customerId}", response_model=schemas.Customer)
async def get_customer(
    customerId: int, db: AsyncSession = Depends(get_session)
):
    return await service.get_customer(db, customerId)


@router.put("/customers/{customerId}", response_model=schemas.Customer)
async def update_customer(
    customerId: int,
    customer: schemas.Customer,
    db: AsyncSession = Depends(get_session)
):
    return await service.update_customer(db, customerId, customer)


@router.delete("/customers/{customerId}", response_model=None)
async def delete_customer(
    customerId: int, db: AsyncSession = Depends(get_session)
):
    await service.delete_customer(db, customerId)
