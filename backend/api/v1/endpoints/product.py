from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.product_model import ProductModel
from schemas.product_schema import ProductSchema
from core.deps import get_session


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProductSchema)
async def post_product(product: ProductSchema, db: AsyncSession = Depends(get_session)):
    """
    Endpoint adiciona um novo produto ao database.
    """
    new_product = ProductModel(
        barcode=product.barcode,
        barcode_type=product.barcodeType,
        product=product.product,
        size=product.size,
        size_unit=product.sizeUnit,
        volume=product.volume,
        volume_unit=product.volumeUnit,
        weight=product.weight,
        weight_unit=product.weightUnit,
        location=product.location,
        id_location=product.idLocation,
        unit_price=product.unitPrice,
        wholesale_quant=product.wholesaleQuant,
        wholesale_unit_price=product.wholesaleUnitPrice
    )

    db.add(new_product)
    await db.commit()

    return new_product


@router.get('/', response_model=List[ProductSchema])
async def get_products(db: AsyncSession = Depends(get_session)):
    """
    Endpoint retorna todos os produtos cadastrados.
    """
    async with db as session:
        query = select(ProductModel)
        result = await session.execute(query)
        products: list[ProductModel] = result.scalars().all()

        return products


@router.get('/{product_id}', response_model=ProductSchema, status_code=status.HTTP_200_OK)
async def get_product(product_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProductModel).filter(ProductModel.id == product_id)
        result = await session.execute(query)
        product = result.scalar_one_or_none()

        if product:
            return product
        else:
            raise HTTPException(
                detail='Product not found.',
                status_code=status.HTTP_404_NOT_FOUND
            )


@router.put('/{product_id}', response_model=ProductSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_product(product_id: int, product: ProductSchema, db: AsyncSession = Depends(get_session)):
    """
    Endpoint atualiza um produto específico.
    """
    async with db as session:
        query = select(ProductModel).filter(ProductModel.id == product_id)
        result = await session.execute(query)
        product_up = result.scalar_one_or_none()

        if product_up:
            product_up.barcode = product.barcode,
            product_up.barcode_type = product.barcodeType,
            product_up.product = product.product,
            product_up.size = product.size,
            product_up.size_unit = product.sizeUnit,
            product_up.volume = product.volume,
            product_up.volume_unit = product.volumeUnit,
            product_up.weight = product.weight,
            product_up.weight_unit = product.weightUnit,
            product_up.location = product.location,
            product_up.id_location = product.idLocation,
            product_up.unit_price = product.unitPrice,
            product_up.wholesale_quant = product.wholesaleQuant,
            product_up.wholesale_unit_price = product.wholesaleUnitPrice

            await session.commit()

            return product_up
        else:
            raise HTTPException(
                detail='Product not found.',
                status_code=status.HTTP_404_NOT_FOUND
            )


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_session)):
    """
    Endpoint deleta um produto específico.
    """
    async with db as session:
        query = select(ProductModel).filter(ProductModel.id == product_id)
        result = await session.execute(query)
        product_del = result.scalar_one_or_none()

        if product_del:
            await session.delete(product_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(
                detail='Product not found.',
                status_code=status.HTTP_404_NOT_FOUND
            )