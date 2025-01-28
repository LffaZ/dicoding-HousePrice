# House Price Prediction with Joblib Deployment
## Project Overview
This project aims to predict house prices based on various features using machine learning techniques. The dataset is from the Kaggle competition "House Prices: Advanced Regression Techniques". The goal is to preprocess the data, train multiple models, evaluate them, and deploy the best model using Joblib for real-time predictions.

This project is special because it marks my first attempt at **model deployment**, where I used **Joblib** to save and deploy the trained model. The **Gradient Boosting Regressor (GBR)** model was selected for deployment due to its high performance, achieving an **R² score of 0.889065**.

## Project Structure
The project is organized as follows:
  ```bash
  House-Price-Prediction/
  ├── data/                          # Folder containing raw dataset files
  │   ├── train.csv                  # Training dataset
  │   ├── test.csv                   # Testing dataset
  │   ├── sample_submission.csv      # Kaggle submission sample
  │   └── data.json                  # Input data for model prediction (JSON format)
  │
  ├── models/                        # Folder where models are saved
  │   ├── gbr_model.joblib           # Saved Gradient Boosting Regressor model (Joblib format)
  │   ├── gbr_model.pkl              # Saved Gradient Boosting Regressor model (Pickle format)
  │
  ├── notebooks/                     # Folder containing Jupyter Notebooks
  │   └── model.ipynb                # Notebook for EDA, preprocessing, and model training
  │
  ├── src/                           # Folder containing Python scripts
  │   ├── model.py                   # Python script for model training and evaluation
  │   ├── testing_deploy.py          # Script for testing the deployment of the model
  │
  ├── requirements.txt               # Python dependencies required for the project
  ├── .gitignore                     # Gitignore file to exclude unnecessary files (models, data, etc.)
  └── README.md                      # Project documentation (this file)
  ```

## Steps and Workflow
This project follows a clear sequence of steps:
1. **Data Collecting**
2. **Data Loading**
3. **Data Cleaning**
4. **Exploratory Data Analysis (EDA)**
5. **Data Splitting**
6. **Modelling**
    - Least-Angle Regression (LARS)
    - Linear Regression (LR)
    - Gradient Boosting Regressor (GBR)
7. **Deployment**

## Installation

To run this project, you'll need Python 3.x and the necessary dependencies. Follow these steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/LffaZ/house-price-prediction.git
   cd house-price-prediction
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   
## Usage
### Training the Model
1. Load and preprocess the data:
   - Load the data from train.csv and test.csv.
   - Perform necessary preprocessing, which is implemented in model.ipynb and model.py.
2. Train the models:
   The models used in this project include:
   - Least-Angle Regression (LARS)
   - Linear Regression (LR)
   - Gradient Boosting Regressor (GBR) – Best-performing model.
3. Evaluate the models:
   - The performance of the models is evaluated using R² scores, with the best model being GBR with an R² of 0.889065.
### Deploying the model:
1. Run the Flask API to serve the model locally:
   ```bash
    python -m testing_deploy
    
2. Make predictions:
    - Once the Flask app is running, you can send data for prediction using the following PowerShell command:
      ```powershell
       Invoke-RestMethod -Uri "http://127.0.0.1:5000/predict" -Method Post -Headers @{ "Content-Type" = "application/json" } -Body (Get-Content -Raw -Path "data.json")

## Acknowledgements
- This project uses the [House Prices: Advanced Regression Techniques dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) from Kaggle for training and testing.
- Special thanks to **Dicoding** for providing the course material that helped in building this project.

