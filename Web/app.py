import os
import pandas as pd
import requests
from flask import Flask
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
 
# function to print sentiments 
# of the sentence. 

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def sentiment_scores(): 
    url = 'https://api.yomomma.info/'

    response = requests.get(url)

    joke = response.json()

    sentence = joke['joke']
    sentiment = "Neutral"

    analyser = SentimentIntensityAnalyzer()

  
    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 
  
    # polarity_scores method of SentimentIntensityAnalyzer 
    # oject gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sid_obj.polarity_scores(sentence) 

      # decide sentiment as positive, negative and neutral 
    if sentiment_dict['compound'] >= 0.05 : 
        sentiment = "Positive"
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        sentiment = "Negative"
  
    else : 
        sentiment = "Neutral"

    Score = str(sentiment_dict['compound'])
    sentiment = str(sentiment)
    #print(Score)
      
    Result = (f'The Joke reads: {sentence}.\nCompound sentiment score is : {Score}. Joke Rated As {sentiment}') 
    return Result
   # ("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
   # ("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    #("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
  
    
# Driver code 
if __name__ == "__main__" :
    app.run(debug=True)
    

    
  

    