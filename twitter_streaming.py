# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
access_token = "Enter Your Acces Token"
access_token_secret = "Enter Your Token Secret"
consumer_key = "Enter Your Consumer Key"
consumer_secret = "Enter Your Consumer Secret"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        print dataxQzmLV9SWrXYQJORUWvDH6AB60mpTvGY48VVm55GK8s3SP5lRc
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    # This handles Twitter authentification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
