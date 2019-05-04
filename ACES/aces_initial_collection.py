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

########## Finding Tweets via keywords ##########
print "-----------------------------------------------------------------------------"
print "Searching for ACES related tweets..."
print "----------------------------- @ACES_UMD Queries -----------------------------"
# Iterate through Queries, storing tweets in dictionary
for query in aces_umd_queries:
    search_results = api.search(q=query,count=100)
    data[query] = search_results
    print "Added " + str(len(search_results)) + " tweets from " + query + " query"

print "----------------------------- ACES + UMD Queries -----------------------------"
# Iterate through Queries, storing tweets in dictionary
for query in aces_plus_umd_queries:
    search_results = api.search(q=query,count=100)
    data[query] = search_results
    print "Added " + str(len(search_results)) + " tweets from " + query + " query"

print "----------------------------- ACES + Maryland Queries -----------------------------"
# Iterate through Queries, storing tweets in dictionary
for query in aces_maryland_queries:
    search_results = api.search(q=query,count=100)
    data[query] = search_results
    print "Added " + str(len(search_results)) + " tweets from " + query + " query"

print "----------------------------- ACES + CS query -----------------------------"
# Iterate through Queries, storing tweets in dictionary
for query in aces_cs_queries:
    search_results = api.search(q=query,count=100)
    data[query] = search_results
    print "Added " + str(len(search_results)) + " tweets from " + query + " query"
