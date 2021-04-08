from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_news = mongo.db.news.find_one()

    # Return template and data
    return render_template("index.html", mars_news= mars_news)



# function from scrape_mars.py file and load the data into MongoDB
@app.route("/scrape")
def scraper():
    # create a collection
    news = mongo.db.news

    mars_data = scrape_mars.scrape()

    news.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)


