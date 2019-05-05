import tweepy
import json

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

# Create data structure to store data
data = {}

# @ACES_UMD Queries
aces_umd_queries = ["@ACES_UMD", "@ACES_UMD :(", "@ACES_UMD :)", "@ACES_UMD:media", "@ACES_UMD:images", "@ACES_UMD:links"]

# ACES + UMD Queries
aces_plus_umd_queries = ["ACES UMD", "ACES UMD :(", "ACES UMD :)", "ACES UMD:media", "ACES UMD:images", "ACES UMD:links"]

# ACES + Maryland Queries
aces_maryland_queries = ["ACES Maryland", "ACES Maryland :(", "ACES Maryland :)", "ACES Maryland:media", "ACES Maryland:images", "ACES Maryland:links"]

# ACES + CS Queries
aces_cs_queries = ["ACES CS", "ACES CS :(", "ACES CS :)", "ACES CS:media", "ACES CS:images", "ACES CS:links"]

# Utility method to add tweet fields to data dictionary
def add_tweet_fields(query, tweet):
    # Null checks
    if tweet.place == None or tweet.coordinates == None:
        data[query].append({
            "id": tweet.id,
            "created_at": str(tweet.created_at),
            "text": tweet.text,
            "user_name": tweet.user.screen_name,
            "user_location": tweet.user.location,
            "user_verified": tweet.user.verified,
            "user_follower_count": tweet.user.followers_count,
            "user_time_zone": tweet.user.time_zone,
            "user_language": tweet.user.lang,
            "country": None,
            "country_code": None,
            "place_full_name": None,
            "coordinates": [],
            "retweet_count": tweet.retweet_count,
            "favorite_count": tweet.favorite_count,
            "tweet_language": tweet.lang
        })
    else:
        data[query].append({
            "id": tweet.id,
            "created_at": str(tweet.created_at),
            "text": tweet.text,
            "user_name": tweet.user.screen_name,
            "user_location": tweet.user.location,
            "user_verified": tweet.user.verified,
            "user_follower_count": tweet.user.followers_count,
            "user_time_zone": tweet.user.time_zone,
            "user_language": tweet.user.lang,
            "country": tweet.place.country,
            "country_code": tweet.place.country_code,
            "place_full_name": tweet.place.full_name,
            "coordinates": tweet.coordinates,
            "retweet_count": tweet.retweet_count,
            "favorite_count": tweet.favorite_count,
            "tweet_language": tweet.lang
        })

########## Finding Tweets via keywords ##########
print "-----------------------------------------------------------------------------"
print "Searching for ACES related tweets..."
print "----------------------------- @ACES_UMD Queries -----------------------------"
# Iterate through Queries, storing tweets in dictionary
for query in aces_umd_queries:
    search_results = api.search(q=query,count=100)
    data[query] = []
    for tweet in search_results:
        add_tweet_fields(query, tweet)
    print "Added " + str(len(search_results)) + " tweets from " + query + " query"

print "----------------------------- ACES + UMD Queries -----------------------------"
# Iterate through Queries, storing tweets in dictionary
for query in aces_plus_umd_queries:
    search_results = api.search(q=query,count=100)
    data[query] = []
    for tweet in search_results:
        add_tweet_fields(query, tweet)
    print "Added " + str(len(search_results)) + " tweets from " + query + " query"

print "----------------------------- ACES + Maryland Queries -----------------------------"
# Iterate through Queries, storing tweets in dictionary
for query in aces_maryland_queries:
    search_results = api.search(q=query,count=100)
    data[query] = []
    for tweet in search_results:
        add_tweet_fields(query, tweet)
    print "Added " + str(len(search_results)) + " tweets from " + query + " query"

print "----------------------------- ACES + CS query -----------------------------"
# Iterate through Queries, storing tweets in dictionary
for query in aces_cs_queries:
    search_results = api.search(q=query,count=100)
    data[query] = []
    for tweet in search_results:
        add_tweet_fields(query, tweet)
    print "Added " + str(len(search_results)) + " tweets from " + query + " query"

# Export data to json file
with open("aces_data.json", "w") as fp:
    json.dump(data, fp)
