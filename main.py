import tweepy
import cv2

#put your credentials in parentheses
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

#Connect to API with credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#making a simple tweet with a image
imagePath = "img1.png"
status = "Atualizações: parte de visão OK no meu pc mas ainda n testei como vai se comportar na rasp. To usando um classficador genérico só por enquanto, porque devo começar a levantar o meu próprio banco. Fiquem com a foto do teste da vez 🥺"
api.update_status_with_media(status=status,filename=imagePath)