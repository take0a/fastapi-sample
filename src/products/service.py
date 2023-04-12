from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from . import models, schemas


async def get_product(db: AsyncSession, productId: int) -> models.Product:
    result = await (db.execute(select(models.Product).filter(
        models.Product.productId == productId)))
    product = result.first()
    if product is None:
        raise HTTPException(status_code=404, detail="product not found")
    return product[0]


async def create_product(db: AsyncSession, product: schemas.Product):
    db_product = models.Product(
        productId=product.productId,
        name=product.name,
        pricePerUnit=product.pricePerUnit)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


async def update_product(
        db: AsyncSession, productId: int, product: schemas.Product
):
    original = await get_product(db, productId)
    original.name = product.name
    original.pricePerUnit = product.pricePerUnit
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_product(db: AsyncSession, productId: int):
    original = await get_product(db, productId)
    await db.delete(original)
    await db.commit()
