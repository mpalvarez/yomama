import os
import pandas as pd
import requests
from flask import Flask, render_template
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pymongo
from flask_pymongo import PyMongo

 
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/joke"
mongo = PyMongo(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
# function to print sentiments 
# of the sentence.
def get_joke():
    conn = "mongodb://localhost:27017/joke"
    client = pymongo.MongoClient(conn)

# Select database and collection to use
    db = client.store_inventory
    collection = db.produce
    url = 'https://api.yomomma.info/'

    response = requests.get(url)

    joke = response.json()
    
    db.collection.insert_one(joke)
    
    return joke

@app.route("/sentiment")
def sentiment_scores(): 
    
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)

    # connect to mongo db and collection
    db = client.store_inventory
    collection = db.produce
    
    sentence = db.collection.find()
  
    sentiment = "Neutral"

    analyser = SentimentIntensityAnalyzer()

  
    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 
  
    # polarity_scores method of SentimentIntensityAnalyzer 
    # oject gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
    
    print(sentiment_dict)

      # decide sentiment as positive, negative and neutral 
    if sentiment_dict['compound'] >= 0.05 : 
        sentiment = "Positive"
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        sentiment = "Negative"
  
    else : 
        sentiment = "Neutral"

    Score = sentiment_dict['compound']
    sentiment = sentiment
    #print(Score)
      
    Result = [{'joke': sentence, 'score': Score, 'sentiment': sentiment}]
    return render_template("index.html", Result = Result)

  
    
# Driver code 
if __name__ == "__main__" :
    app.run(debug=True)
    

    
  

    