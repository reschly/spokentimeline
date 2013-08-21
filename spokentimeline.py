from twitter import *
import pyttsx
import APIKEYS

                
''' MYCREDS.txt has the following format:
oauthtokenvalue
oauthsecretvalue
'''

def getTwitterByConfig():
    oauth_token, oauth_secret = read_token_file("MYCREDS.txt")
    twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, APIKEYS.SPOKENTIMELINE_CONSUMERKEY, APIKEYS.SPOKENTIMELINE_CONSUMERSECRET))
    return twitter

def printTimeline(timeline):
    for tweet in timeline:
        try:
            print(tweet['user']['screen_name'] + " at " + tweet['created_at'] + " tweeted " + tweet['text']);
        except UnicodeEncodeError:
            pass;

def formatTimeline(timeline):
    result = []
    for tweet in timeline:
        result.append(tweet['user']['screen_name'] + " at " + tweet['created_at'] + " tweeted " + tweet['text'])
    return result
        
def getTimeline(twitter):
    return twitter.statuses.home_timeline()
 

def getSpeechEngine():
    return pyttsx.init()

def speakTimeline(engine, timeline):
    for tweet in formatTimeline(timeline):
        engine.say(tweet)
    
if __name__ == "__main__":
    t = getTwitterByConfig()
    timeline = getTimeline(t)
    printTimeline(timeline)
    engine = getSpeechEngine()
    speakTimeline(engine, timeline)