from .db_connection import Base

from sqlalchemy import (
    column,
    Integer
)

class category(Base):
    __tablename__ = "category"

    id = column(Integer, primary_key=True)