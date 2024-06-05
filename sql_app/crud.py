from sqlalchemy.orm import Session

from . import models, schemas


def get_dinosaur(db: Session, dinosaur_id: int):
    return db.query(models.Dinosaur).filter(models.Dinosaur.id == dinosaur_id).first()


def get_dinosaurs(db: Session):
    return db.query(models.Dinosaur).all()


def get_dinosaurs_filtered(db: Session, filters: dict):
    filtered_dinosaurs = db.query(models.Dinosaur)

    for property_name, value in filters.items():
        if not hasattr(models.Dinosaur, property_name):
            raise ValueError(
                f"Property '{property_name}' does not exist in Dinosaur model."
            )

        property_attr = getattr(models.Dinosaur, property_name)
        filtered_dinosaurs = filtered_dinosaurs.filter(property_attr == value)

    return filtered_dinosaurs


def bulk_create_dinosaurs(db: Session, dinosaurs: list[schemas.DinosaurCreate]):
    db.add_all([models.Dinosaur(**dino.model_dump()) for dino in dinosaurs])
    db.commit()
