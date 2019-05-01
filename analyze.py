import tweepy

########## Setting up API ##########
# API keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Create authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Set access token and secret
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

########## Analyzing my timeline ##########
# Get tweets from my timeline
public_tweets = api.home_timeline()

# Iterate through public_tweets
for tweet in public_tweets:
    print tweet.text

########## Analyzing tweets from a specific user ##########
# Pull tweets from the NY times
name = "nytimes"

# Number of tweets to Pull
tweet_count = 20

# Get tweets
nytimes_tweets = api.user_timeline(id=name, count=tweet_count)

# Iterate through tweets
for tweet in nytimes_tweets:
    print tweet.text

########## Finding Tweets via keyword ##########
# Search for Tweets with keyword Trump
query = "Trump"

# Language code
language = "en"

# Search query
search_results = api.search(q=query, lang=language)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
