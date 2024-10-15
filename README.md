# Building-a-Data-Warehouse-to-store-data

This project involves scraping images from Telegram channels, performing object detection using YOLO, and exposing the detection results through a REST API using FastAPI. It consists of multiple tasks including data scraping, cleaning, object detection, and API development.

---

## Table of Contents

- [Project Overview]
- [Technologies Used]
- [Data Scraping]
- [Data Cleaning and Transformation]
- [Object Detection Using YOLO]
- [Task 4 - Exposing Data via FastAPI]
- [Installation]
- [Database Setup]
- [API Endpoints]
- [Running the Application]
- [Logging](#logging)


---

## Project Overview

This project involves the following tasks:
1. Scraping images from Telegram channels.
2. Cleaning and transforming the scraped data.
3. Performing object detection on the images using YOLO (You Only Look Once).
4. Storing the detection results in a PostgreSQL database.
5. Exposing the results through an API using FastAPI.


---

## Technologies Used

- **Python**: Main programming language.
- **Telethon**: Library for scraping data from Telegram.
- **YOLOv5**: Object detection model.
- **OpenCV**: Image processing library.
- **SQLAlchemy**: ORM for database management.
- **PostgreSQL**: Relational database to store object detection results.
- **FastAPI**: Web framework to expose the API.
- **Uvicorn**: ASGI server for running FastAPI.
- **DBT**: For data transformation.
- **Pydantic**: For data validation and serialization.

---

##  Data Scraping

### Objective
Scrape images from the specified Telegram channels using the **Telethon** library.

### Steps:
1. Set up the **Telethon** client using your API ID and API hash.
2. Scrape images from the channels **CheMed123** and **Lobelia4Cosmetics**.
3. Store the raw scraped data (images and metadata) into temporary storage.
4. Implement logging to track the scraping process.

### Required Libraries:
- **Telethon**: `pip install telethon`
  
---

##  Data Cleaning and Transformation

### Objective
Clean the scraped data, handle duplicates, and transform it for further processing.

### Steps:
1. **Removing Duplicates**: Remove any duplicate images or metadata.
2. **Handling Missing Values**: Fill in missing metadata fields or drop incomplete records.
3. **Standardizing Formats**: Ensure image formats and metadata are consistent.
4. **Data Validation**: Validate that the images are usable for object detection (e.g., resolution checks).
5. **Storing Cleaned Data**: Store the cleaned data in PostgreSQL.

### Tools:
- **DBT (Data Build Tool)**: Used for transforming and validating the data.
  - Install DBT: `pip install dbt`
  - Initialize project: `dbt init my_project`
  - Run transformations: `dbt run`
  - Test transformations: `dbt test`

---

##  Object Detection Using YOLO

### Objective
Run object detection on the cleaned images using the pre-trained YOLOv5 model.

### Steps:
1. **Set up YOLOv5**:
   - Clone YOLOv5 repository: `git clone https://github.com/ultralytics/yolov5.git`
   - Install dependencies: `pip install -r yolov5/requirements.txt`
2. **Load Images**: Load the cleaned images into the YOLO model for object detection.
3. **Run Object Detection**: Detect objects and retrieve the bounding box coordinates, confidence scores, and labels.
4. **Store Detection Results**: Save the detection results in PostgreSQL.

### Required Libraries:
- **YOLOv5**
- **OpenCV**: `pip install opencv-python`
- **Torch**: `pip install torch torchvision`
  
---

##  Exposing Data via FastAPI

### Objective
Create a REST API to expose the object detection results using FastAPI.

### Steps:
1. **Install FastAPI and Uvicorn**:
   ```bash
   pip install fastapi uvicorn
