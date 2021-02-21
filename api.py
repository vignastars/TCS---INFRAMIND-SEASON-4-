from flask import Flask
from flask_restful import Resource, Api, reqparse
import random

app = Flask(_name_)
api = Api(app)

WELLNESS = {
    "Steps":random.randint(4000, 10000),
    "Body Temperature":(round(random.uniform(36.5,37.5),1)),
    "Blood Pressure":random.randint(90,120),
    "Respiration":random.randint(12,16),
    "Glucose":random.randint(72,140),
    "Heart Rate":random.randint(60,100),
    "Oxygen Saturation":random.randint(95,100)
    
}

Diabetes = {
    "Steps":random.randint(4000, 10000),
    "Body Temperature":(round(random.uniform(36.5,37.5),1)),
    "Blood Pressure":random.randint(90,120),
    "Respiration":random.randint(12,16),
    "Glucose":random.randint(200,350),
    "Heart Rate":random.randint(60,100),
    "Oxygen Saturation":random.randint(95,100)
    
}

Prediabetes = {
    "Steps":random.randint(4000, 10000),
    "Body Temperature":(round(random.uniform(36.5,37.5),1)),
    "Blood Pressure":random.randint(90,120),
    "Respiration":random.randint(12,16),
    "Glucose":random.randint(140,199),
    "Heart Rate":random.randint(60,100),
    "Oxygen Saturation":random.randint(95,100)
    
}

parser=reqparse.RequestParser()

class wellnessRecord(Resource):
    def get(self):
        return WELLNESS

    def post(self):
        parser.add_argument("Disease")
        args = parser.parse_args()
        dis=args["Disease"]
        if dis=="Diabetes":
            return Diabetes
        elif dis=="Prediabetes":
            return Prediabetes



api.add_resource(wellnessRecord, '/wRecord/')

if _name_ == "_main_":
  app.run(debug=True)