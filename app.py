import os
import pandas as pd
import requests
from Flask import flasl
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyze
 
# function to print sentiments 
# of the sentence. 
def sentiment_scores(sentence): 
  
    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 
  
    # polarity_scores method of SentimentIntensityAnalyzer 
    # oject gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
      
    return ("Overall sentiment dictionary is : " + sentiment_dict + "Sentence Overall Rated As", end = " ") 
   # ("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
   # ("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    #("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
  
    
  
    # decide sentiment as positive, negative and neutral 
    if sentiment_dict['compound'] >= 0.05 : 
        print("Positive") 
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        print("Negative") 
  
    else : 
        print("Neutral") 
  
  
    
# Driver code 
if __name__ == "__main__" : 

    analyser = SentimentIntensityAnalyzer()

    ##API URL

    url = 'https://api.yomomma.info/'

    response = requests.get(url)

    joke = response.json()

    yomama = joke['joke']
  
    print("\n1st statement :") 
    sentence = yomama
  
    # function calling 
    sentiment_scores(sentence) 
  
    print("\n2nd Statement :") 
    sentence = "study is going on as usual"
    sentiment_scores(sentence) 
  
    print("\n3rd Statement :") 
    sentence = "I am vey sad today."
    sentiment_scores(sentence) 

