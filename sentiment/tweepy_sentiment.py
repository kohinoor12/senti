from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy
import numpy as np
import pandas as pd

class Import_tweet_sentiment:

	consumer_key="user consumer_key"
	consumer_secret="user consumer_secret"
	access_token="user access_token"
	access_token_secret="user access_token_secret"

	def tweet_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		return df

	def get_tweets(self, handle):
		# auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		# auth.set_access_token(self.access_token, self.access_token_secret)
		# auth_api = API(auth)

		# account = handle
		# item = auth_api.user_timeline(id=account,count=20)
		# df = self.tweet_to_data_frame(item)

		# all_tweets = []
		# for j in range(20):
		# 	all_tweets.append(df.loc[j]['Tweets'])

		df = pd.read_csv(r'text_emotion.csv')
		handle = handle.replace("@", "")
		matching_rows = df[df['author'] == handle]
		matching_rows = matching_rows['content'].copy()
		all_tweets = matching_rows.values.tolist()

		return all_tweets

	def get_hashtag(self, hashtag):
		# auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		# auth.set_access_token(self.access_token, self.access_token_secret)
		# auth_api = API(auth)

		# account = hashtag
		# all_tweets = []

		# for tweet in tweepy.Cursor(auth_api.search, q=account, lang='en').items(20):
		# 	all_tweets.append(tweet.text)

		df = pd.read_csv(r'text_emotion.csv')

		# handle = handle.replace("#", "")

		def check_handle(text):
			return hashtag.lower() in text.lower()

		# Apply the function to the 'text' column
		filtered_df = df[df['content'].apply(check_handle)]

		all_tweets = filtered_df['content'].tolist()

		return all_tweets
