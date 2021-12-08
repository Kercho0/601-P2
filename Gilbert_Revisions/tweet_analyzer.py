from t import twitter_auth
from searchparty import searchparty
from analyzer import analyzer
import pandas as pd
import tweepy
import datetime
import sys
from classify import classify
from sentiment import sentiment

def tweet_analyzer(keyword_in, date_in, number_in):
   # keyword= input("Enter keyword to search for: ")
    keyword = keyword_in

    today=datetime.datetime.today().strftime('%Y-%m-%d')
        
    #input_date=input("Enter Date (yyyy-mm-dd, press enter for today): ")
    input_date = date_in

    if input_date: 
        try: 
            year, month, day = input_date.split('-')
        except ValueError:
            print("Please use correct date input format")
            sys.exit(1)
        valid = True
        try:
            datetime.date(int(year), int(month), int(day))
        except ValueError: 
            valid = False

    
    #max_number=int(input("Number of tweets to retrieve: ") )    
    max_number=number_in
    if input_date == '':
        today = today
    elif not valid: 
        print ("Date input is not valid")
        sys.exit(1)
    else:
        today = input_date
    try:
        analyzer(keyword, today, max_number)
    except: 
        print("Please make sure your input is correct")
        sys.exit(1)
