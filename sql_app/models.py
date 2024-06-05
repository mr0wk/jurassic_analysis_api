from sqlalchemy import Column, Float, Integer, String

from .database import Base


class Dinosaur(Base):
    __tablename__ = "dinosaurs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    diet = Column(String, index=True)
    period = Column(String, index=True)
    lived_in = Column(String, index=True)
    type = Column(String, index=True)
    length = Column(Float, index=True)
    species = Column(String, index=True)
