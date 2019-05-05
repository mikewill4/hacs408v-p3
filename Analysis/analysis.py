import json

with open("../ACES/aces_data.json", "r") as file:
    data = json.load(file)

# Check that queries have been loaded
for key in data.keys():
    print key

# Quick test that json was loaded and attributes can be accessed
print data["ACES UMD"][0]["text"]
print data["ACES UMD"][0]["country"]
print data["ACES UMD"][0]["created_at"]
