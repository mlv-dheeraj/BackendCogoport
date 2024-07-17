from sqlalchemy import Column, Integer, String, DateTime, ForeignKey , Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import enum

class ServiceTypeEnum(enum.Enum):
    FCL = "FCL"
    AIR = "AIR"
    TRUCK="TRUCK"

class StatusTypeEnum(enum.Enum):
    PENDING="PENDING"
    COMPLETED="COMPLETED"
    CANCELLED="CANCELLED"

class BaseTable(Base):
    __tablename__ = 'base'

    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, index=True, nullable=False)
    destination = Column(String, nullable=False)
    Date=Column(DateTime,nullable=True)
    service_type = Column(Enum(ServiceTypeEnum), nullable=False)
    status=Column(Enum(StatusTypeEnum),nullable=False)
    Commodity=Column(String,nullable=True)
    SubCommodity=Column(String,nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)


    container = relationship("CONTAINER", back_populates="search")
    package = relationship("PACKAGE", back_populates="search")
    truck = relationship("TRUCK", back_populates="search")



