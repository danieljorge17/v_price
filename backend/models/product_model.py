from sqlalchemy import Column, Integer, String, Float

from core.configs import settings


class ProductModel(settings.DBBaseModel):
    __tablename__ = 'produts'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    barcode: str = Column(String(250), nullable=False)
    barcode_type: str = Column(String(255), nullable=True)
    product: str = Column(String(255), nullable=False)
    size: float = Column(Float, nullable=True)
    size_unid: str = Column(String(255), nullable=True)
    volume: float = Column(Float, nullable=True)
    volume_unid: str = Column(String(255), nullable=True)
    weight: float = Column(Float, nullable=True)
    weight_unid: str = Column(String(255), nullable=True)
    location: str = Column(String(255), nullable=False)
    id_location: int = Column(Integer, nullable=True)
    unit_price: float = Column(Float, nullable=False)
    wholesale_quant: int = Column(Integer, nullable=True)
    wholesale_unit_price: float = Column(Float, nullable=True)
