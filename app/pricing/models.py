# SQLAlchemy models
from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

from app.base.model import BaseModel


class Pricing(BaseModel):
    __tablename__ = "pricing"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    price = Column(Float, nullable=False, index=True)
    sku_id = Column(Integer, ForeignKey("sku.id"), index=True)
    sku = relationship("SKU", backref="pricing")
