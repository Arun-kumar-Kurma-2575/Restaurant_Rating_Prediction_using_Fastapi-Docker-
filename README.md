# Restaurant Rating Prediction

## Description

This project is a machine learning application that predicts restaurant ratings based on various features such as country code, city, average cost for two, currency, table booking availability, online delivery, price range, rating color, rating text, votes, and cuisines. The application consists of a backend API built with FastAPI and a frontend web interface built with Streamlit, all containerized using Docker for easy deployment.

The machine learning model is a Random Forest model trained on a cleaned dataset of restaurant data. The model development process is documented in the `Model_Development.ipynb` Jupyter notebook.

## Features

- Predict restaurant ratings using a trained Random Forest model
- Web-based user interface for inputting restaurant features
- RESTful API(FastAPI) for programmatic access
- Containerized deployment using Docker and Docker Compose
- Clean and intuitive UI with custom styling

## Project Structure

```
.
├── cleaned_dataset.csv          # Cleaned dataset used for model training
├── docker-compose.yaml          # Docker Compose configuration for multi-service setup
├── Model_Development.ipynb      # Jupyter notebook for model development and training
├── Restaurant_rating_Final.py   # Final Python script for model training (if applicable)
├── backend/                     # Backend service directory
│   ├── Dockerfile               # Dockerfile for backend service
│   ├── main.py                  # FastAPI application for prediction API
│   ├── requirements.txt         # Python dependencies for backend
│   └── Restaurant_rating_RF.pkl # Trained Random Forest model (pickle file)
└── frontend/                    # Frontend service directory
    ├── Dockerfile               # Dockerfile for frontend service
    ├── frontend.py              # Streamlit application for web interface
    └── requirements.txt         # Python dependencies for frontend
```

## Prerequisites

- Docker installed on your system
- Docker Compose installed (usually comes with Docker Desktop)

## Installation and Execution

1. **Clone or navigate to the project directory:**
   ```
   cd .../Restaurant_Rating_Prediction
   ```

2. **Build and run the application using Docker Compose:**
   ```
   docker-compose up --build
   ```

   This command will:
   - Build the backend and frontend Docker images
   - Start the backend service on port 8000
   - Start the frontend service on port 8501

3. **Access the application:**
   - Frontend (Streamlit web interface): Open your browser and go to `http://localhost:8501`
   - Backend API: The API is available at `http://localhost:8000`

## Usage

### Web Interface
1. Open the frontend at `http://localhost:8501`
2. Fill in the restaurant features in the provided form
3. Click the "Predict Rating" button to get the predicted rating

### API Usage
You can also make direct API calls to the backend:

- **GET /**: Welcome message
- **POST /predict**: Predict rating

Example API request using curl:
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "country_code_encoded": 1,
       "city_encoded": 2,
       "Average_Cost_for_two": 50,
       "currency_encoded": 1,
       "table_booking_encoded": 0,
       "online_delivery_encoded": 1,
       "price_range_encoded": 2,
       "Rating_color_encoded": 1,
       "rating_text_encoded": 2,
       "votes": 100,
       "cuisines_encoded": [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}'
```

## Model Development

To understand the model development process:
1. Open `Model_Development.ipynb` in Jupyter Notebook or JupyterLab
2. Run the cells to see data preprocessing, model training, and evaluation

## Stopping the Application

To stop the running containers:
```
docker-compose down
```

