import tweepy
import cv2

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)
vid = cv2.VideoCapture(0)

try:
    tweet = client.create_tweet(text="testando...")
    print(tweet)
except: 
    print("deu pau")