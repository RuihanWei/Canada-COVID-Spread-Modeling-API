from flask import Flask
app = Flask(__name__)
import pymongo

@app.route("/")
def hello():
  return "Hello World!"



if __name__ == "__main__":
  app.run(debug=True)






#############  db creation for reference
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["covid"]
# collection = db['csv']

# db creation code
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["covid"]
# db.create_collection('csv')
# # collection = db['csv']
# print(client.list_database_names())
