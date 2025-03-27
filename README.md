# 🚗 **Vehicle Maintenance Predictor**  

## 📌 Overview  

**Vehicle Maintenance Predictor** is a **Flask-based machine learning web application** designed to predict vehicle maintenance needs based on various input parameters such as **mileage, vehicle age, fuel type, engine size, and more**. The application leverages a **Logistic Regression model** trained on a **cleaned dataset of vehicle records** to provide accurate maintenance insights.  

---

## ✨ **Key Features**  

✅ **User-Friendly Web Interface** – Enter vehicle details and get instant maintenance predictions.  
✅ **Machine Learning-Powered Predictions** – Uses **Logistic Regression** to assess maintenance needs.  
✅ **Multiple Input Factors Considered** – Mileage, fuel type, engine size, brake condition, tire condition, etc.  
✅ **Efficient Data Processing** – Utilizes **Pandas & NumPy** for handling vehicle data.  
✅ **Cross-Origin Resource Sharing (CORS)** – Enables API access from different sources.  

---

## 📂 **Project Structure**  

```
📁 Vehicle-Maintenance-Predictor  
│── app.py                  # Main Flask application  
│── templates/  
│   └── index.html          # Web interface for input & prediction  
│── static/                 # CSS, JS, and other assets  
│── LogisticRegressionModel.pkl  # Trained ML model  
│── Cleaned_Vehicle_Data.csv    # Preprocessed dataset  
│── requirements.txt        # Dependencies  
│── README.md               # Project documentation  
```  

---

## 🚀 **Getting Started**  

### 1️⃣ **Prerequisites**  
Ensure **Python 3.x** is installed on your system. Install required dependencies:  

```bash
pip install -r requirements.txt
```  

### 2️⃣ **Run the Application**  
Start the Flask app with:  

```bash
python app.py
```  

---

## 📊 **Input Parameters**  

The application accepts the following **vehicle attributes** for prediction:  

- **Vehicle Model**  
- **Mileage**  
- **Reported Issues**  
- **Vehicle Age**  
- **Fuel Type**  
- **Transmission Type**  
- **Engine Size**  
- **Tire Condition**  
- **Brake Condition**  
- **Battery Status**  

---

## 🛠 **Tech Stack**  

- **Flask** – Backend framework  
- **Scikit-Learn** – Machine learning model  
- **Pandas & NumPy** – Data processing  
- **HTML & CSS** – Frontend interface  

---

## 📈 **Future Enhancements**  

✅ **Improve model accuracy** using **Random Forest, XGBoost, or deep learning**.  
✅ **Integrate real-time vehicle data** for dynamic insights.  
✅ **Deploy the application on cloud platforms** for wider accessibility.  
✅ **Enhance UI/UX** with a more interactive design.  


