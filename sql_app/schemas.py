from pydantic import BaseModel


class DinosaurBase(BaseModel):
    name: str
    diet: str
    period: str
    lived_in: str
    type: str
    length: float
    species: str


class DinosaurCreate(DinosaurBase):
    pass


class Dinosaur(DinosaurBase):
    id: int

    class Config:
        from_attributes = True
