from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle   # coverts python object to Byte stream-- basically sends python data over network
import pandas as pd  # library used for reading and writing in csv files
import numpy as np

app=Flask(__name__)
cors = CORS(app)
model=pickle.load(open('LogisticRegressionModel.pkl','rb')) # bytestream data of logistic regression model  is loaded to model
car=pd.read_csv('Cleaned_Vech_Data.csv') # with help of pandas we are reading csv file

@app.route('/',methods=['GET','POST'])
def index():
    Vehicle_Models =sorted(car['Vehicle_Model'].unique())
    Fuel_Types =sorted(car['Fuel_Type'].unique())
    Transmission_Types =sorted(car['Transmission_Type'].unique())
    Tire_Conditions =sorted(car['Tire_Condition'].unique())
    Brake_Conditions = sorted(car['Brake_Condition'].unique())
    Battery_Statuss  = sorted(car['Battery_Status'].unique())


    Vehicle_Models.insert(0,'Select Model')
    return render_template('index.html',Vehicle_Models=Vehicle_Models,Fuel_Types=Fuel_Types,Transmission_Types=Transmission_Types,Tire_Conditions=Tire_Conditions,Brake_Conditions=Brake_Conditions,Battery_Statuss=Battery_Statuss)


@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    Vehicle_Model =request.form.get('Vehicle_Model')
    Mileage=request.form.get('Mileage')
    Reported_Issues=request.form.get('Reported_Issues')
    Vehicle_Age=request.form.get('Vehicle_Age')
    Fuel_Type=request.form.get('Fuel_Type')
    Transmission_Type=request.form.get('Transmission_Type')
    Engine_Size=request.form.get('Engine_Size')
    Tire_Condition=request.form.get('Tire_Condition')
    Brake_Condition=request.form.get('Brake_Condition')
    Battery_Status=request.form.get('Battery_Status')


    prediction=model.predict(pd.DataFrame(columns=['Vehicle_Model','Mileage','Reported_Issues','Vehicle_Age','Fuel_Type','Transmission_Type','Engine_Size','Tire_Condition','Brake_Condition','Battery_Status'],
                              data=np.array([Vehicle_Model,Mileage,Reported_Issues,Vehicle_Age,Fuel_Type,Transmission_Type,Engine_Size,Tire_Condition,Brake_Condition,Battery_Status]).reshape(1, 10)))
    print(prediction)
    return str(np.round(prediction[0],2))



if __name__=='__main__':
    app.run()

