from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars_app
collection = db.mars_scraped_data



@app.route("/")
def home():

    mars = list(db.mars_scraped_data.find())
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape_data():

     mars = scrape_mars.scrape()
     db.mars_scraped_data.drop()

	 db.mars_scraped_data.insert_one(mars)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

