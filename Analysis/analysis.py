# Libraries
import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
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

# Iniitalize values for plot
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
