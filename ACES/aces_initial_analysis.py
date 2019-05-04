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

########## Finding Tweets via keyword ##########
print "-----------------------------------------------------------------------------"
print "Searching for ACES related tweets..."
print "----------------------------- @ACES_UMD query -----------------------------"
# Search for Tweets with keyword @ACES_UMD
query = "@ACES_UMD"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- @ACES_UMD negative query -----------------------------"
# Search for Tweets with keyword @ACES_UMD and a negative attitude
query = "@ACES_UMD :("

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- @ACES_UMD positive query -----------------------------"
# Search for Tweets with keyword @ACES_UMD and a positive attitude
query = "@ACES_UMD :)"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- @ACES_UMD media query -----------------------------"
# Search for Tweets with keyword @ACES_UMD and containing an image or video
query = "@ACES_UMD:media"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- @ACES_UMD images query -----------------------------"
# Search for Tweets with keyword @ACES_UMD and containing an image
query = "@ACES_UMD:images"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- @ACES_UMD url query -----------------------------"
# Search for Tweets with keyword @ACES_UMD and containing a URL
query = "@ACES_UMD:links"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + UMD query -----------------------------"
# Search for Tweets with keywords ACES and UMD
query = "ACES UMD"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + UMD negative query -----------------------------"
# Search for Tweets with keywords ACES and UMD and a negative attitude
query = "ACES UMD :("

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + UMD positive query -----------------------------"
# Search for Tweets with keywords ACES and UMD and a positive attitude
query = "ACES UMD :)"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + UMD media query -----------------------------"
# Search for Tweets with keywords ACES and UMD and containing an image or video
query = "ACES UMD:media"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + UMD images query -----------------------------"
# Search for Tweets with keywords ACES and UMD and containing an image
query = "ACES UMD:images"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + UMD url query -----------------------------"
# Search for Tweets with keywords ACES and UMD and containing a URL
query = "ACES UMD:links"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + Maryland query -----------------------------"
# Search for Tweets with keywords ACES and Maryland
query = "ACES Maryland"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + Maryland negative query -----------------------------"
# Search for Tweets with keywords ACES and Maryland and a negative attitude
query = "ACES Maryland :("

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + Maryland positive query -----------------------------"
# Search for Tweets with keywords ACES and Maryland and a positive attitude
query = "ACES Maryland :)"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + Maryland media query -----------------------------"
# Search for Tweets with keywords ACES and Maryland and containing an image or video
query = "ACES Maryland:media"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + Maryland images query -----------------------------"
# Search for Tweets with keywords ACES and Maryland and containing an image
query = "ACES Maryland:images"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + Maryland url query -----------------------------"
# Search for Tweets with keywords ACES and Maryland and containing a URL
query = "ACES Maryland:links"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + CS query -----------------------------"
# Search for Tweets with keywords ACES and CS
query = "ACES CS"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + CS negative query -----------------------------"
# Search for Tweets with keywords ACES and CS and a negative attitude
query = "ACES CS :("

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + CS positive query -----------------------------"
# Search for Tweets with keywords ACES and CS and a positive attitude
query = "ACES CS :)"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + CS media query -----------------------------"
# Search for Tweets with keywords ACES and CS and containing an image or video
query = "ACES CS:media"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + CS images query -----------------------------"
# Search for Tweets with keywords ACES and CS and containing an image
query = "ACES CS:images"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"

print "----------------------------- ACES + CS url query -----------------------------"
# Search for Tweets with keywords ACES and CS and containing a URL
query = "ACES CS:links"

# Search query
search_results = api.search(q=query,count=100)

# Iterate through search_results
for tweet in search_results:
    print tweet.user.screen_name,"Tweeted:",tweet.text
print str(len(search_results)) + " total results"
