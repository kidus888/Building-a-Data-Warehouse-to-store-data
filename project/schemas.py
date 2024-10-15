from pydantic import BaseModel

class DetectionResultBase(BaseModel):
    image_path: str
    class_label: str
    confidence: float
    x1: int
    y1: int
    x2: int
    y2: int

class DetectionResultCreate(DetectionResultBase):
    pass

class DetectionResult(DetectionResultBase):
    id: int

    class Config:
        orm_mode = True
