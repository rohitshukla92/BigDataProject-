from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json 
import os
import sys


# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="Pr5qbY4DjgNq7sbDgCo8sK3fu"
consumer_secret="VSJASScDTyKzddAQue2TdDB98dn4qCX22IgVTiuMBp1wPuPXeZ"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="930208627708882944-EtqVQ8YYXINx9Z7mZoGvVkKvb6Rrxl4"
access_token_secret="IoP6Wb1628namo6s3AZWgsMtzpCgWpJjHmrj5zNSkLodj"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        try:
            saveFile=open('twitDB.csv','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'failed ondata',str(e)
            time.sleep(5)  

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['hunger','malnourishment','famine','starvation','underweight'])