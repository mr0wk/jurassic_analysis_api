from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from sql_app import SessionLocal, crud, schemas

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/dinosaurs/", response_model=list[schemas.Dinosaur])
def read_dinosaurs(
    db: Session = Depends(get_db),
    name: str = Query(None),
    diet: str = Query(None),
    period: str = Query(None),
    lived_in: str = Query(None),
    type: str = Query(None),
    length: float = Query(None),
    species: str = Query(None),
):
    filters = {
        "name": name,
        "diet": diet,
        "period": period,
        "lived_in": lived_in,
        "type": type,
        "length": length,
        "species": species,
    }
    if not any(filters.values()):
        return crud.get_dinosaurs(db)
    else:
        filters = {k: v for k, v in filters.items() if v is not None}

        try:
            return crud.get_dinosaurs_filtered(db, filters)
        except ValueError as e:
            return HTTPException(status_code=400, detail=str(e))
