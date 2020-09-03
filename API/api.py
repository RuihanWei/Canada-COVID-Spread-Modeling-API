import flask

app = flask.Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def hello():
  return flask.render_template("index.html", token="hello")


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
