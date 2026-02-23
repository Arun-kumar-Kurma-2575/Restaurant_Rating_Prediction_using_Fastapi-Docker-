from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from fastapi.responses import JSONResponse

with open('Restaurant_rating_RF.pkl','rb') as f:
       model=pickle.load(f)

app=FastAPI()

class User_input(BaseModel):
        country_code_encoded:int
        city_encoded:int
        Average_Cost_for_two:int
        currency_encoded:int
        table_booking_encoded:int
        online_delivery_encoded:int
        price_range_encoded:int
        Rating_color_encoded:int
        rating_text_encoded:int
        votes:int
        cuisines_encoded:list[int]

@app.get('/')
def home():
    return {'message':"welcome to the Restaurant Rating Prediction App"}

@app.post('/predict')
def predict_rating(input_data:User_input):
       
        country_code_encoded=input_data.country_code_encoded
        city_encoded=input_data.city_encoded
        Average_Cost_for_two=input_data.Average_Cost_for_two
        currency_encoded=input_data.currency_encoded
        table_booking_encoded=input_data.table_booking_encoded
        online_delivery_encoded=input_data.online_delivery_encoded
        price_range_encoded=input_data.price_range_encoded
        Rating_color_encoded=input_data.Rating_color_encoded
        rating_text_encoded=input_data.rating_text_encoded
        votes=input_data.votes
        cuisines_encoded=input_data.cuisines_encoded
        
        data = [
        country_code_encoded, city_encoded, Average_Cost_for_two, currency_encoded,
        table_booking_encoded, online_delivery_encoded, price_range_encoded,
        Rating_color_encoded, rating_text_encoded, votes
        ] + cuisines_encoded

        prediction=model.predict([data])[0]

        return JSONResponse(status_code=200,content={'Predicted_rating':prediction})




