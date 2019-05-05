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

# @UofMaryland Queries
uofmaryland_queries = ["@UofMaryland", "@UofMaryland :(", "@UofMaryland :)", "@UofMaryland:media", "@UofMaryland:images", "@UofMaryland:links"]

# UMCP Queries
umcp_queries = ["UMCP", "UMCP :(", "UMCP :)", "UMCP:media", "UMCP:images", "UMCP:links"]

# university maryland college park Queries
umd_college_park_queries = ["university maryland college park", "university maryland college park :(", "university maryland college park :)", "university maryland college park:media", "university maryland college park:images", "university maryland college park:links"]

# university maryland cp Queries
umd_cp_queries = ["university maryland cp", "university maryland cp :(", "university maryland cp :)", "university maryland cp:media", "university maryland cp:images", "university maryland cp:links"]

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

########## Finding Tweets via keyword ##########
print "-----------------------------------------------------------------------------"
print "Searching for UMD related tweets..."
print "----------------------------- UofMaryland Query -----------------------------"
# Iterate through Queries, storing tweets in dictionary
for query in uofmaryland_queries:
    search_results = api.search(q=query,count=100)
    data[query] = []
    for tweet in search_results:
        add_tweet_fields(query, tweet)
    print "Added " + str(len(search_results)) + " tweets from " + query + " query"

print "----------------------------- UMCP Query -----------------------------"
# Iterate through Queries, storing tweets in dictionary
for query in umcp_queries:
    search_results = api.search(q=query,count=100)
    data[query] = []
    for tweet in search_results:
        add_tweet_fields(query, tweet)
    print "Added " + str(len(search_results)) + " tweets from " + query + " query"

print "----------------------------- university + maryland + college + park Query -----------------------------"
# Iterate through Queries, storing tweets in dictionary
for query in umd_college_park_queries:
    search_results = api.search(q=query,count=100)
    data[query] = []
    for tweet in search_results:
        add_tweet_fields(query, tweet)
    print "Added " + str(len(search_results)) + " tweets from " + query + " query"

print "----------------------------- university + maryland + cp Query -----------------------------"
# Iterate through Queries, storing tweets in dictionary
for query in umd_cp_queries:
    search_results = api.search(q=query,count=100)
    data[query] = []
    for tweet in search_results:
        add_tweet_fields(query, tweet)
    print "Added " + str(len(search_results)) + " tweets from " + query + " query"

# Export data to json file
with open("umd_data.json", "w") as fp:
    json.dump(data, fp)
