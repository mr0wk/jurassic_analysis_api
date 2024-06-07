import pandas as pd
from sqlalchemy.orm import Session

from sql_app import engine, models

from .crud import bulk_create_dinosaurs
from .database import SessionLocal
from .schemas import DinosaurCreate

csv_file_path = "sql_app/data.csv"

df = pd.read_csv(csv_file_path)

df = df.drop(columns=["taxonomy", "named_by", "link"])

dinosaur_data = df.to_dict(orient="records")

dinosaur_list = [DinosaurCreate(**dino) for dino in dinosaur_data]

db: Session = SessionLocal()

try:
    models.Base.metadata.create_all(bind=engine)
    bulk_create_dinosaurs(db, dinosaur_list)
finally:
    db.close()
