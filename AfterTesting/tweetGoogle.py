#!/usr/bin/env python3
from google.cloud import language_v1 as lg
import os
import tweepy #https://github.com/tweepy/tweepy
import json
import tweet 
import Gcloud
import sys

def score(outNLP):
	if outNLP[0] <= -0.6:
		return print('people are showing a lot of negative sentiment')
	elif -0.6 < outNLP[0] <= -0.25:
		return print('people are showing few negative sentiment')
	elif -0.25 < outNLP[0] <= 0.25:
		return print('people are showing natural sentiment')
	elif 0.25 < outNLP[0] <= 0.6:
		return print('people are showing few positive sentiment ')
	elif outNLP[0] > 0.6:
		return print('people are showing a lot of positive sentiment')
	elif outNLP = None:
		return print('error from NLP')

def main(name):
	
	try:
		searchOut = tweet.searchTweets(name)
		print(f'what currently people are tweeting:\n{searchOut}')
		if len(searchOut)==0:
			print('no result from your search')
		else:
			out = Gcloud.anaSentiment(searchOut)
			#print(out)
			score(out)
	except:
		print('twitter API does not like what you typed')




if __name__=="__main__":
	name = sys.argv[1]
	main(name)
