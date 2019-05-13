# Libraries
import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import operator
#import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap

# Load json from aces_data.json file
with open("../ACES/aces_data.json", "r") as file:
    aces_data = json.load(file)

# Load json from umd_data.json file
with open("../UMD/umd_data.json", "r") as file:
    umd_data = json.load(file)

########## UMD Analysis ##########

########## Spatial analysis ##########
# Extract tweets that have location data
umd_tweet_coordinates = []
for query,tweets in umd_data.items():
    for tweet in tweets:
        if len(tweet["coordinates"]) > 0:
            umd_tweet_coordinates.append(tweet)
print len(umd_tweet_coordinates)

# Creating the map
# Set dimension of figure
#dpi=96
#plt.figure(figsize=(2600/dpi, 1800/dpi), dpi=dpi)

# Make map background
#m = Basemap(llcrnrlon=-180, llcrnrlat=-65, urcrnrlon=180, urcrnrlat=80)
#m.drawmapboundary(fill_color="#A6CAE0", linewidth=0)
#m.fillcontinents(color="grey", alpha=0.3)
#m.drawcoastlines(linewidth=0.1, color="white")

# Set colors for each point depending on continent

# Add points
# m.scatter()

# Copyright
#plt.text(-170, -58, "Plot created with Python and the Basemap library", ha="left", va="bottom", size="9", color="#555555")

# Save as png
#plt.savefig("test_bubble_map_umd.png", bbox_inches="tight")

########## Sentiment analysis ##########
# Get positive and negative tweets
positive_sentiment_umd = []
negative_sentiment_umd = []
for query,tweets in umd_data.items():
    if ":)" in query:
        positive_sentiment_umd.extend(umd_data[query])
    if ":(" in query:
        negative_sentiment_umd.extend(umd_data[query])

# Iniitalize values for plot
sentiment_objects = ["Positive", "Negative"]
y_pos = np.arange(len(sentiment_objects))
sentiment_values_umd = [len(positive_sentiment_umd), len(negative_sentiment_umd)]

# Plot
plt.bar(y_pos, sentiment_values_umd, align="center", alpha=0.5, width=0.25)
plt.xticks(y_pos, sentiment_objects)
plt.ylabel("# of Tweets")
plt.xlabel("Sentiment")
plt.title("Sentiment Analysis of UMD")
plt.show(block=True)

########## Social anlysis ##########
umd_tweet_users = {}
most_retweets_umd = -1
most_favorites_umd = -1
for query,tweets in umd_data.items():
    for tweet in tweets:
        if tweet["user_name"] not in umd_tweet_users:
            umd_tweet_users[tweet["user_name"]] = tweet["user_follower_count"]
        if tweet["retweet_count"] > most_retweets_umd:
            most_retweets_umd = tweet["retweet_count"]
            most_retweeted_tweet_umd = tweet
        if tweet["favorite_count"] > most_favorites_umd:
            most_favorites_umd = tweet["favorite_count"]
            most_favorited_tweet_umd = tweet

# Most popular tweets
print most_retweeted_tweet_umd["text"]
print most_favorited_tweet_umd["text"]

# 10 most popular users
sorted_users = sorted(umd_tweet_users.items(), key=operator.itemgetter(1), reverse=True)
top_users = {}
for i in range(0,10):
    top_users[sorted_users[i][0]] = sorted_users[i][1]
y_pos = np.arange(10)
plt.bar(y_pos, top_users.values(), align="center", alpha=0.5, width=0.25)
plt.xticks(y_pos, top_users.keys())
plt.ylabel("# of Followers")
plt.xlabel("User")
plt.title("Social Analysis of UMD")
plt.show(block=True)

########## ACES Analysis ##########

########## Spatial analysis ##########

########## Sentiment analysis ##########
positive_sentiment_aces = []
negative_sentiment_aces = []
for query,tweets in aces_data.items():
    if ":)" in query:
        positive_sentiment_aces.extend(aces_data[query])
    if ":(" in query:
        negative_sentiment_aces.extend(aces_data[query])

# Initialize values for plot
sentiment_objects = ["Positive", "Negative"]
y_pos = np.arange(len(sentiment_objects))
sentiment_values_aces = [len(positive_sentiment_aces), len(negative_sentiment_aces)]

# Plot
plt.bar(y_pos, sentiment_values_aces, align="center", alpha=0.5, width=0.25)
plt.xticks(y_pos, sentiment_objects)
plt.ylabel("# of Tweets")
plt.xlabel("Sentiment")
plt.title("Sentiment Analysis of ACES")
plt.show(block=True)

########## Social anlysis ##########
aces_tweet_users = {}
most_retweets_aces = -1
most_favorites_aces = -1
for query,tweets in aces_data.items():
    for tweet in tweets:
        if tweet["user_name"] not in aces_tweet_users:
            aces_tweet_users[tweet["user_name"]] = tweet["user_follower_count"]
        if tweet["retweet_count"] > most_retweets_aces:
            most_retweets_aces = tweet["retweet_count"]
            most_retweeted_tweet_aces = tweet
        if tweet["favorite_count"] > most_favorites_aces:
            most_favorites_aces = tweet["favorite_count"]
            most_favorited_tweet_aces = tweet

# Most popular tweets
print most_retweeted_tweet_aces["text"]
print most_favorited_tweet_aces["text"]

# 10 most popular users
sorted_users = sorted(aces_tweet_users.items(), key=operator.itemgetter(1), reverse=True)
top_users = {}
for i in range(0,10):
    top_users[sorted_users[i][0]] = sorted_users[i][1]
y_pos = np.arange(10)
plt.bar(y_pos, top_users.values(), align="center", alpha=0.5, width=0.25)
plt.xticks(y_pos, top_users.keys())
plt.ylabel("# of Followers")
plt.xlabel("User")
plt.title("Social Analysis of ACES")
plt.show(block=True)
