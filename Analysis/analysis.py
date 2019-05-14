# Libraries
import json
import numpy as np
import matplotlib.pyplot as plt
import operator
import folium
import pandas as pd
import geocoder

# Load json from aces_data.json file
with open("../ACES/aces_data.json", "r") as file:
    aces_data = json.load(file)

# Load json from umd_data.json file
with open("../UMD/umd_data.json", "r") as file:
    umd_data = json.load(file)

########## UMD Analysis ##########

########## Spatial analysis ##########
# Extract tweets that have location data
umd_tweet_coordinates = {}
for query,tweets in umd_data.items():
    for tweet in tweets:
        tweet_location = "No country or city for " + tweet["user_name"] + "\' tweet"
        if tweet["user_location"] != None and len(tweet["user_location"]) > 0 and "\\u" not in tweet["user_location"]:
            tweet_location = tweet["user_location"]
        if len(tweet["coordinates"]) > 0:
            umd_tweet_coordinates[tweet_location] = tweet["coordinates"]
        elif "No country" not in tweet_location:
            print("processing " + tweet_location)
            curr_coords = { "coordinates": geocoder.bing(tweet_location).latlng }
            print(curr_coords)
            umd_tweet_coordinates[tweet_location] = curr_coords

# Create empty map
umd_map = folium.Map(location=[20, 0], tiles="Mapbox bright", zoom_start=2)

# Add markers to map
for location,coords in umd_tweet_coordinates.items():
    if coords["coordinates"] != None:
        folium.Marker([coords["coordinates"][1], coords["coordinates"][0]], popup=location).add_to(umd_map)
    else:
        folium.Marker([coords["coords"][0], coords["coords"][1]], popup=location).add_to(umd_map)

# Save map
umd_map.save("../Plots/umd_spatial_analysis.html")

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
print(most_retweeted_tweet_umd["text"])
print(most_favorited_tweet_umd["text"])

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
# Extract tweets that have location data
aces_tweet_coordinates = {}
for query,tweets in aces_data.items():
    for tweet in tweets:
        tweet_location = "No country or city for " + tweet["user_name"] + "\' tweet"
        if tweet["user_location"] != None and len(tweet["user_location"]) > 0 and "\\u" not in tweet["user_location"]:
            tweet_location = tweet["user_location"]
        if len(tweet["coordinates"]) > 0:
            aces_tweet_coordinates[tweet_location] = tweet["coordinates"]
        elif "No country" not in tweet_location:
            print("processing " + tweet_location)
            curr_coords = { "coords": geocoder.bing(tweet_location).latlng }
            print(curr_coords)
            aces_tweet_coordinates[tweet_location] = curr_coords

# Create empty map
aces_map = folium.Map(location=[20, 0], tiles="Mapbox bright", zoom_start=2)

# Add markers to map
for location,coords in aces_tweet_coordinates.items():
    if coords["coordinates"] != None:
        folium.Marker([coords["coordinates"][1], coords["coordinates"][0]], popup=location).add_to(aces_map)
    else:
        folium.Marker([coords["coords"][0], coords["coords"][1]], popup=location).add_to(aces_map)

# Save map
aces_map.save("../Plots/aces_spatial_analysis.html")

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
print(most_retweeted_tweet_aces["text"])
print(most_favorited_tweet_aces["text"])

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
