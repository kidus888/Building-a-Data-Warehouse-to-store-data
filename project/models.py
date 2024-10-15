from sqlalchemy import Column, Integer, String, Float
from .database import Base

class DetectionResult(Base):
    __tablename__ = 'detection_results'

    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String, index=True)
    class_label = Column(String)
    confidence = Column(Float)
    x1 = Column(Integer)
    y1 = Column(Integer)
    x2 = Column(Integer)
    y2 = Column(Integer)
