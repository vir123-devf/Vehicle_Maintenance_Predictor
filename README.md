🚗 Vehicle Maintenance Predictor

📌 Overview

Vehicle Maintenance Predictor is a Flask-based machine learning web application that predicts the maintenance needs of a vehicle based on multiple input parameters like mileage, vehicle age, fuel type, and more. The application uses a Logistic Regression model trained on a cleaned dataset of vehicle records to provide insights into potential maintenance requirements.

✨ Features

🔹 Interactive Web Interface: Users can enter vehicle details and get maintenance predictions instantly.

🔹 Machine Learning-Based Prediction: Uses Logistic Regression for determining maintenance needs.

🔹 Multiple Input Parameters: Takes vehicle attributes such as mileage, fuel type, engine size, tire condition, brake condition, etc.

🔹 Data Processing with Pandas & NumPy: Efficiently handles and processes vehicle data for predictions.

🔹 Cross-Origin Resource Sharing (CORS) Enabled: Allows API access from different origins.

📂 Project Structure

📁 Vehicle-Maintenance-Predictor
│── app.py              # Main Flask application
│── templates/
│   └── index.html      # Web interface for input and prediction
│── static/             # CSS, JS, and assets (if needed)
│── LogisticRegressionModel.pkl  # Trained ML model
│── Cleaned_Vech_Data.csv  # Preprocessed vehicle dataset
│── requirements.txt    # Dependencies
│── README.md           # Project documentation

🚀 Getting Started

1️⃣ Prerequisites

Ensure you have Python 3.x installed on your system. Install required dependencies using:

pip install -r requirements.txt

2️⃣ Running the Application

Run the Flask application using the following command:

python app.py

Then, open your browser and visit:

http://127.0.0.1:5000/

📊 Input Parameters

The application accepts the following parameters for prediction:

Vehicle Model

Mileage

Reported Issues

Vehicle Age

Fuel Type

Transmission Type

Engine Size

Tire Condition

Brake Condition

Battery Status

🛠 Tech Stack

Flask - Backend framework

Scikit-Learn - Machine learning model

Pandas & NumPy - Data processing

HTML, CSS - Frontend interface

📈 Future Improvements

✅ Enhance model accuracy with more advanced ML models (Random Forest, XGBoost, etc.)
✅ Add real-time vehicle data integration
✅ Deploy the application on cloud platforms
✅ Improve UI/UX for better user experience

🤝 Contributing

Feel free to fork the repository, submit issues, and suggest improvements. Any contributions are welcome! 🚀
