from typing import Optional

from pydantic import BaseModel as SCBaseModel


class ProductSchema(SCBaseModel):
    id: Optional[int]
    barcode: str
    barcodeType: Optional[str]
    product: str
    size: Optional[float]
    sizeUnit: Optional[str]
    volume: Optional[float]
    volumeUnit: Optional[str]
    weight: Optional[float]
    weightUnit: Optional[str]
    location: str
    idLocation: Optional[int]
    unitPrice: float
    wholesaleQuant: Optional[int]
    wholesaleUnitPrice: Optional[float]

    class Config:
        orm_mode = True