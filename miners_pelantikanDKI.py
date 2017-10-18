# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Variables that contains the user credentials to access Twitter API
access_token = "151969580-z800m24tNl2KcVvbeZU7RRLWjBxZgj8rppSLYyx5"
access_token_secret = "JVtPz9X3ImJWgzslHHXZV6qs0wTS6gg00v28IzKMwTGSm"
consumer_key = "SeNhgUMbQSyF3OzTgGsUVbNar"
consumer_secret = "LjFAIYwFyXrKycPSgPnzeafRHNe6SXj8VhP4GDTLcUwLmTrVzU"


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
    stream.filter(track=['anies', 'sandi', 'dki', 'jakartabaru', 'ahok', 'djarot', 'anies-sandi', 'badja'])
