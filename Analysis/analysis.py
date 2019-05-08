# Libraries
import json
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

########## Social anlysis ##########

########## ACES Analysis

########## Spatial analysis ##########

########## Sentiment analysis ##########

########## Social anlysis ##########
