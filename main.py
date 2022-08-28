import tweepy
import cv2

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
imagePath = "cinzinha.jpg"
status = "fala pessoal, criei esse bot aqui inspirado no @PepitoTheCat pra registrar o tanto de gato que sobe na minha cama durante o dia, ta em construção ainda e vai demorar p ficar bom porque tenho que arrumar mt coisa mas espero que fique decente\n\no github é: https://github.com/KauaOrtiz/Bot-Gatitos"
api.update_status_with_media(status=status,filename=imagePath)