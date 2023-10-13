from sqlalchemy import Boolean, Column, String, DateTime
from datetime import datetime

from database import Base


class BaseModel(Base):
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    created_by = Column(String, nullable=False)
    updated_by = Column(String, nullable=False)
    deleted_by = Column(String, nullable=True)
    active = Column(Boolean, nullable=False, default=True)
