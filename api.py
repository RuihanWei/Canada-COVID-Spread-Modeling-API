import csv
import json
import urllib

import requests
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
import pymongo
from pymongo import MongoClient

csv_folder_url = 'https://raw.githubusercontent.com/RuihanWei/Canada-COVID-Spread-Modeling-API/master/Prediction_results/'
json_url = "https://raw.githubusercontent.com/RuihanWei/Canada-COVID-Spread-Modeling-API/master/db_dump.json"


@app.route("/test", methods=['GET'])
def hello():
  return jsonify({"hello": "hello"})

@app.route("/getForecast/<case>/<country>/<province>", methods=['GET'])
def getForecast(case, country, province):
  # client = MongoClient("mongodb+srv://Jeremy:<pswd>@cluster0.ptx5w.mongodb.net/covid?retryWrites=true&w=majority")
  # db = client["covid"]
  # collection = db['csv']
  # query = {
  #   "case": str(case),
  #   "country": country,
  #   "province": province
  # }
  # res = collection.find_one(query)

  resp = requests.get(json_url)
  json_db = json.loads(resp.text)
  res = ""
  for entry in json_db:
    if entry["case"] == str(case) and entry["country"] == country and entry["province"] == province:
      res = entry
      break

  # data1 = []
  # with open('Prediction_results/' + res["filename"], newline='') as inputfile:
  #   for row in csv.reader(inputfile):
  #     data1.append(row)

  data = []
  # # csv_url = 'https://raw.githubusercontent.com/RuihanWei/Canada-COVID-Spread-Modeling-API/master/Prediction_results/100%25_Canada_Ontario.csv'
  # df = pd.read_csv(csv_folder_url+"/"+urllib.parse.quote_plus(res["filename"]))
  df = pd.read_csv(csv_folder_url+"/"+urllib.parse.quote_plus(res["filename"]))
  data.append(df.columns.tolist())
  data.append(df.values.tolist()[0])

  return jsonify({"dates": data[0],
                  "values": data[1]})

@app.route("/getCases/<country>/<province>")
def getCases(country, province):
  # client = MongoClient("mongodb+srv://Jeremy:<pswd>@cluster0.ptx5w.mongodb.net/covid?retryWrites=true&w=majority")
  # db = client["covid"]
  # collection = db['csv']
  # query = {
  #   "country": country,
  #   "province": province
  # }
  # res = collection.find(query)

  res = []
  resp = requests.get(json_url)
  json_db = json.loads(resp.text)
  for entry in json_db:
    if entry["country"] == country and entry["province"] == province:
      res.append(entry)

  cases = []
  for x in res:
    if x["case"] not in cases:
      cases.append(x["case"])
  return jsonify({"cases": cases})


@app.route("/getProvinces")
def getProvinces():
  # client = MongoClient("mongodb+srv://Jeremy:pswd@cluster0.ptx5w.mongodb.net/covid?retryWrites=true&w=majority")
  # db = client["covid"]
  # collection = db['csv']
  #
  # # modify if new feature involves more countries
  # query = {
  #   "country": "Canada"
  # }
  # res = collection.find(query)

  res = []
  resp = requests.get(json_url)
  json_db = json.loads(resp.text)
  for entry in json_db:
    if entry["country"] == "Canada":
      res.append(entry)

  province = []
  for x in res:
    if x["province"] not in province:
      province.append(x["province"])
  return jsonify({"provinces": province})


if __name__ == "__main__":
  app.run(debug=True)







#############  db creation/deletion for reference
# mLab
# cluster = MongoClient("mongodb+srv://Jeremy:<password>@cluster0.ptx5w.mongodb.net/covid?retryWrites=true&w=majority")
# db = cluster["covid"]
# collection = db['csv']
# collection.insert_one({"test": "test"})

# db deletion
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["covid"]
# collection = db['csv']
# collection.delete_many({})

#db creation code
# db = client["covid"]
# db.create_collection('csv')
# # collection = db['csv']
# print(client.list_database_names())
