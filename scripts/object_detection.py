import torch
import os
import cv2
import logging
import psycopg2
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    filename='object_detection.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load environment variables (if using .env file for DB credentials)
load_dotenv()

# Database credentials
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Connect to PostgreSQL database
def connect_db():
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        logging.info("Connected to the database")
        return connection
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
        return None

# Create table for storing object detection results
def create_detection_table(cursor):
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS detection_results (
        id SERIAL PRIMARY KEY,
        image_path TEXT,
        class_label TEXT,
        confidence FLOAT,
        x1 INT,
        y1 INT,
        x2 INT,
        y2 INT
    );
    '''
    cursor.execute(create_table_query)

# Run YOLO object detection on an image
def detect_objects(image_path, model):
    # Load image with OpenCV
    img = cv2.imread(image_path)
    if img is None:
        logging.warning(f"Image not found: {image_path}")
        return []

    # Use YOLO model to perform object detection
    results = model(img)
    return results

# Store detection results in the PostgreSQL database
def store_detection_results(cursor, image_path, results):
    for result in results.xyxy[0]:  # xyxy format: [x1, y1, x2, y2, confidence, class]
        x1, y1, x2, y2, confidence, cls = result.tolist()
        class_label = model.names[int(cls)]
        cursor.execute(
            '''
            INSERT INTO detection_results (image_path, class_label, confidence, x1, y1, x2, y2)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''',
            (image_path, class_label, confidence, int(x1), int(y1), int(x2), int(y2))
        )

# Main function for object detection and saving results
def main():
    # Load pre-trained YOLOv5 model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    model.eval()  # Set the model to evaluation mode

    # Directory containing the scraped images
    image_dir = 'scraped_images'
    images = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith(('.jpg', '.png'))]

    # Connect to PostgreSQL
    connection = connect_db()
    if connection is None:
        return

    cursor = connection.cursor()
    create_detection_table(cursor)

    # Perform object detection on each image and store results
    for image_path in images:
        logging.info(f"Processing image: {image_path}")
        results = detect_objects(image_path, model)
        store_detection_results(cursor, image_path, results)
        logging.info(f"Results stored for image: {image_path}")

    # Commit the transaction and close the connection
    connection.commit()
    cursor.close()
    connection.close()
    logging.info("Database connection closed")

if __name__ == "__main__":
    main()
