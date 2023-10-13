# Pydantic models
from app.base.schema import BaseSchema


class ProductSchema(BaseSchema):
    id: int | None = None
    name: str


class SKUSchema(BaseSchema):
    id: int | None = None
    product_id: int
    name: str
    description: str
    image: str | None = None
