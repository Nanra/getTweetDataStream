# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Variables that contains the user credentials to access Twitter API
access_token = "Enter your acces token"
access_token_secret = "Enter your token secret"
consumer_key = "Enter your Consumer key"
consumer_secret = "Enter Your Consumer Key"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        decoded = json.loads(data)
        print (decoded['user']['screen_name'], decoded['text'].encode('ascii','ignore'))
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
    stream.filter(track=['ridwan', 'kamil', 'dedi', 'mulyadi', 'dedy', 'mizwar', 'pilkada', 'jabar'])
