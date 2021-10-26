#! /usr/bin/env python3


# Imports the Google Cloud client library
from google.cloud import language_v1 as lg
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/media/james/extradrive1/homework/homework/EC601/Project2/ec601-project2-yenyu-b6426ae7a965.json'


# Instantiates a client
client = lg.LanguageServiceClient()

# The text to analyze
text = u"""Harper Lee, believed to be one of the most influential authors to have ever existed, 
famously published only a single novel (up until its controversial sequel was published in 2015 just before her death). 
Lee’s To Kill a Mockingbird was published in 1960 and became an immediate classic of literature. 
The novel examines racism in the American South through the innocent wide eyes of a clever young girl 
named Jean Louise (“Scout”) Finch. Its iconic characters, most notably the sympathetic and just lawyer 
and father Atticus Finch, served as role models and changed perspectives in the United States at a time 
when tensions regarding race were high. To Kill a Mockingbird earned the Pulitzer Prize for fiction in 1961 
and was made into an Academy Award-winning film in 1962, giving the story and its characters further life 
and influence over the American social sphere."""
#needs to be in document form
document = lg.Document(content=text, language = 'en', type_=lg.Document.Type.PLAIN_TEXT)

#analyze document
response = client.analyze_sentiment(document = document, encoding_type = 'UTF32')


sentiment = response.document_sentiment



#print("Text: {}".format(text))
									#score -1 > -0.25 = negative
									# -0.25 > 0.25 = natural
									# 0.25 > 1 = positive
									#magnitude range from 0 - inf

print("Sentiment score = {}, magnitude = {}".format(sentiment.score, sentiment.magnitude))
#print(response.sentences[1].sentiment) #print out each target sentence's sentiment
