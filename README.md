# Fyndme Full Stack Developer Coding Test 

## Sections:  Overview
This project demonstrates the following:
1. **Image Processing and Object Detection** using YOLOv5 for detecting products on a shelf image.
2. **Backend RESTful API Development** using Flask to manage product information.
3. Data Handling and Augmented Reality Integration (Was part of test but not integrated in this test as I have not enough knowledge in AR)


## Section 1/image_processing: Object Detection with YOLOv5

### Requirements
- Python 3.12.6
- Libraries:
  - OpenCV
  - PyTorch
  - NumPy
  - YOLOv5

### Setup Instructions
1. Navigate to the `image_processing` folder:
   cd image_processing
2. Install the dependencies:
    pip install -r requirements.txt
3. Download YOLOv5:
    git clone https://github.com/ultralytics/yolov5.git
    cd yolov5
    pip install -r requirements.txt
    cd ..
4. Add an example image named shelf.jpg to the sample_images folder.
5. Run the detection script:
python yolo_inference.py
6. The detection output will be saved as output.jpg and displayed on the screen.


## Section 2/backend_api: Flask RESTful API
### Requirements
- Python 3.12.6
- Libraries:
    - Flask
    - Flask-RESTful
    - Setup Instructions

1. Navigate to the backend_api folder:
    cd backend_api

2. Install the dependencies:
    pip install -r requirements.txt

3. Run the Flask application:
    python app.py

4. The API will be accessible at http://127.0.0.1:5000

# API Endpoints
1. Get All Products: Endpoint: GET /products
2. Get a Product by ID: Endpoint: GET /products?id=1
3. Add a Product: Endpoint: POST /products
    - Sample json:
    {"name": "Product A", "price": 150.0}
4. Update a Product: Endpoint: PUT /products/1
5. Delete a Product: Endpoint: DELETE /products/1