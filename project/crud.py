from sqlalchemy.orm import Session
from . import models, schemas

# Create a new detection result
def create_detection_result(db: Session, detection_result: schemas.DetectionResultCreate):
    db_result = models.DetectionResult(**detection_result.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

# Get detection result by ID
def get_detection_result(db: Session, result_id: int):
    return db.query(models.DetectionResult).filter(models.DetectionResult.id == result_id).first()

# Get all detection results
def get_detection_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DetectionResult).offset(skip).limit(limit).all()

# Delete a detection result
def delete_detection_result(db: Session, result_id: int):
    db_result = get_detection_result(db, result_id)
    if db_result:
        db.delete(db_result)
        db.commit()
        return True
    return False
