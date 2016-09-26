import tweepy
import profile
import re
from tts import say

WORDS = {
    'read_tweet': {'groups': [['read', 'tweet'], ['get', 'tweet']]},
    'send_tweet': {'groups': [['send', 'tweet'], ['write', 'tweet']]},
}

auth = tweepy.OAuthHandler(profile.data['twi_consumer_key'], profile.data['twi_consumer_secret'])
auth.set_access_token(profile.data['twi_access_token'], profile.data['twi_access_token_secret'])
api = tweepy.API(auth)


def read_tweet():
    public_tweets = api.home_timeline(count=5)
    for tweet in public_tweets:
        if tweet.author.screen_name != 'CommitStrip_fr':
            say('tweet from ' + tweet.author.screen_name)
            text = re.sub(r"(?:\@|https?\://)\S+", "", tweet.text)
            say(text)


def send_tweet():
    api.update_status('msg test')
    say('your tweet has been posted.')
