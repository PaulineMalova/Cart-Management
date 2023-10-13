# SQLAlchemy models
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.base.model import BaseModel


class Product(BaseModel):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)


class SKU(BaseModel):
    __tablename__ = "sku"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("product.id"), index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    image = Column(String, nullable=True)
    product = relationship("Product", lazy="joined")
