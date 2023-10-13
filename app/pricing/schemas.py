# Pydantic models
from app.base.schema import BaseSchema


class PricingSchema(BaseSchema):
    id: int | None = None
    price: float
    sku_id: int
