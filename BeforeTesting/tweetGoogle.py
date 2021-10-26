#!/usr/bin/env python3
from google.cloud import language_v1 as lg
import os
import tweepy #https://github.com/tweepy/tweepy
import json
import tweet 
import testGcloud

searchOut = tweet.searchTweets('HD8xx')
print(f'what currently people are tweeting:\n{searchOut}')

out = testGcloud.anaSentiment(searchOut)
#print(out)
if out[0] <= -0.6:
	print('people are showing a lot of negative sentiment')
elif -0.6 < out[0] <= -0.25:
	print('people are showing few negative sentiment')
elif -0.25 < out[0] <= 0.25:
	print('people are showing natural sentiment')
elif 0.25 < out[0] <= 0.6:
	print('people are showing few positive sentiment ')
elif out[0] > 0.6:
	print('people are showing a lot of positive sentiment')
