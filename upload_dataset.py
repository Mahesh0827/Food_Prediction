from pymongo import MongoClient 
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["food_prediction"]  # Corrected line
collection = db["dataset"]

# Read dataset
df = pd.read_csv("food_dataset.csv")  # replace with your actual CSV path

rec=df.to_dict(orient="record")
collection.insert_many(rec)


