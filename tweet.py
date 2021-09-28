#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json



#Twitter API credentials
consumer_key = 'BLRdMXoMyknp3aC2G8nuvyE2d'#'49124003-IJPd0nEGWYFep6cluAbdvm8Z48Bdl4iw5hTkFoyce'#"Enter the consumer_key"
consumer_secret = 'NRvfjErPFdJRBjpBkzfr9TdLAYoythFXoFe6U6rVuscO0AnzFz'#'WrTrXKfFQtszWGqsK3p4iOLl6Dn6Cwwq3NNAwNlkRgb5Q'#"Enter the consumer_secret"
access_key = '49124003-IJPd0nEGWYFep6cluAbdvm8Z48Bdl4iw5hTkFoyce'#'BLRdMXoMyknp3aC2G8nuvyE2d' #"Enter the access_key"
access_secret = 'WrTrXKfFQtszWGqsK3p4iOLl6Dn6Cwwq3NNAwNlkRgb5Q'#'NRvfjErPFdJRBjpBkzfr9TdLAYoythFXoFe6U6rVuscO0AnzFz'#"Enter the access_secret"


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print( f"...{len(alltweets)} tweets downloaded so far") 

    #write tweet objects to JSON
    file = open('tweet.json', 'w') 
    print( "Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    print( "Done")
    file.close()

def printTweet(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    public_tweets = api.user_timeline(screen_name = screen_name,count=10)
    for tweet in public_tweets:
        print(tweet.text)
    # Get the User object for twitter...
    user = api.get_user(screen_name = screen_name)
    print("="*20)
    print(f'User name: @{user.screen_name}')
    print(f'Total followers: {user.followers_count}')
    print('List of following accounts:')
    for friend in user.friends():
       print(friend.screen_name)
    

def searchTweets(q,count = 20):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    searchResult = api.search_tweets(q = q,count = count)
    for result in searchResult:
        print(result.text)
        #print(searchResult)


    

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@YenyuChen27")
    printTweet("@YenyuChen27")
    searchTweets('Boston University')



    



    
