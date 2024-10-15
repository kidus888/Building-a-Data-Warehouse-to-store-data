from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

# Create FastAPI instance
app = FastAPI()

# Create tables (run once to initialize the DB)
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a detection result
@app.post("/detection_results/", response_model=schemas.DetectionResult)
def create_detection_result(detection_result: schemas.DetectionResultCreate, db: Session = Depends(get_db)):
    return crud.create_detection_result(db, detection_result)

# Get all detection results
@app.get("/detection_results/", response_model=list[schemas.DetectionResult])
def read_detection_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_detection_results(db, skip=skip, limit=limit)

# Get detection result by ID
@app.get("/detection_results/{result_id}", response_model=schemas.DetectionResult)
def read_detection_result(result_id: int, db: Session = Depends(get_db)):
    db_result = crud.get_detection_result(db, result_id)
    if db_result is None:
        raise HTTPException(status_code=404, detail="Detection result not found")
    return db_result

# Delete a detection result
@app.delete("/detection_results/{result_id}", response_model=schemas.DetectionResult)
def delete_detection_result(result_id: int, db: Session = Depends(get_db)):
    success = crud.delete_detection_result(db, result_id)
    if not success:
        raise HTTPException(status_code=404, detail="Detection result not found")
    return {"message": "Detection result deleted successfully"}
