from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session
from . import schemas, service


router = APIRouter()


@router.post("/products", response_model=schemas.Product)
async def create_product(
    product: schemas.Product, db: AsyncSession = Depends(get_session)
):
    return await service.create_product(db, product)


@router.get("/products/{productId}", response_model=schemas.Product)
async def get_product(
    productId: int, db: AsyncSession = Depends(get_session)
):
    return await service.get_product(db, productId)


@router.put("/products/{productId}", response_model=schemas.Product)
async def update_product(
    productId: int,
    product: schemas.Product,
    db: AsyncSession = Depends(get_session)
):
    return await service.update_product(db, productId, product)


@router.delete("/products/{productId}", response_model=None)
async def delete_product(
    productId: int, db: AsyncSession = Depends(get_session)
):
    await service.delete_product(db, productId)
