from flask import Flask, request
from flasgger import Swagger
import pickle
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
Swagger(app)

pickled_model_file = open("pickle_diabetes_model.pkl","rb")
regressor = pickle.load(pickled_model_file)

@app.route('/')    #decorators
def home():
    return "Welcome to diabetes regression"

@app.route('/predict')
def predict_diabetes():
    """Predict the Diabetes
    ---
    parameters:
       -  name: age
          in: query
          type: number
          required: true
       -  name: sex
          in: query
          type: category
          required: true  
       -  name: bmi
          in: query
          type: number
          required: true 
       -  name: bp
          in: query
          type: number
          required: true  
       -  name: s1
          in: query
          type: number
          required: true
       -  name: s2
          in: query
          type: number
          required: true  
       -  name: s3
          in: query
          type: number
          required: true 
       -  name: s4
          in: query
          type: number
          required: true 
       -  name: s5
          in: query
          type: number
          required: true
       -  name: s6
          in: query
          type: number
          required: true             
 
    responses:
        200:
            description: The result is
    """

    age = request.args.get("age")
    sex = request.args.get("sex")
    bmi = request.args.get("bmi")
    bp = request.args.get("bp")
    s1 = request.args.get("s1")
    s2 = request.args.get("s2")
    s3 = request.args.get("s3")
    s4 = request.args.get("s4")
    s5 = request.args.get("s5")
    s6 = request.args.get("s6")

    result = regressor.predict([[age,sex,bmi,bp, s1,s2,s3,s4,s5,s6]])

    return f"The prediction is {result}"

if __name__ == "__main__":
    app.run()