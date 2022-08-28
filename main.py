import tweepy


consumer_key = "G6EBx3VrsRPZ9fdvPv4Tro0aA"
consumer_secret = "n43aOnlhJqFFbLmNEcY1sGGsw36tar4kc84UwuHAd3QulEGzbW"
access_token = "1563536795031089152-GyrgLfkOpCC8ZB536TIGf5BPnKXOBd"
access_token_secret = "0OFuuYU0FtQbIjo3RucUfRDOkZMPX0nnLolXTT9dDshVW"

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

try:
    tweet = client.create_tweet(text="testando...")
    print(tweet)
except:
    print("deu pau")