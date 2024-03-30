from pymongo.mongo_client import MongoClient
import pandas as pd
import json
import urllib.parse

# encoded_password = urllib.parse.quote_plus(password)
# encoded_username = urllib.parse.quote_plus(username)

## uniform resource indentifier
url = f"mongodb+srv://tapankheni:tapankheni@cluster0.blfohxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

## create a new client and connect to server
client = MongoClient(url)

## send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You are sucessfully connected to a MongoDB!")
except Exception as e:
    print(e)

## create database name and collection name
DATABASE_NAME = "wafers_fault_project"
COLLECTION_NAME = "wafers_fault_data"

## read the data as a dataframe 
df = pd.read_csv("/Users/tapankheni/Data_Science/Data Science Projects/Wafers_Fault_Prediction/research/WafersData.csv")
df.drop(["Unnamed: 0"], axis=1, inplace=True)

## convert the data into json
json_record = list(json.loads(df.T.to_json()).values())

## dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
