from twitter import *
import APIKEYS


''' MYCREDS.txt has the following format:
oauthtokenvalue
oauthsecretvalue
'''

def getTwitter():
    oauth_token, oauth_secret = read_token_file("MYCREDS.txt")
    twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, APIKEYS.SPOKENTIMELINE_CONSUMERKEY, APIKEYS.SPOKENTIMELINE_CONSUMERSECRET))
    return twitter

def printTimeline(timeline):
    for tweet in timeline:
        try:
            print(tweet['user']['screen_name'] + " at " + tweet['created_at'] + " tweeted " + tweet['text']);
        except UnicodeEncodeError:
            pass;
        
def getTimeline(twitter):
    return twitter.statuses.home_timeline()
    
if __name__ == "__main__":
    t = getTwitter()
    timeline = getTimeline(t)
    printTimeline(timeline)