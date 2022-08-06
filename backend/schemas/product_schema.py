from typing import Optional

from pydantic import BaseModel as SCBaseModel


class ProductSchema(SCBaseModel):
    id: Optional[int]
    barcode: str
    barcode_type: Optional[str]
    product: str
    size: Optional[float]
    size_unid: Optional[str]
    volume: Optional[float]
    volume_unid: Optional[str]
    weight: Optional[float]
    weight_unid: Optional[str]
    location: str
    id_location: Optional[int]
    unit_price: float
    wholesale_quant: Optional[int]
    wholesale_unit_price: Optional[float]

    class Config:
        orm_mode = True