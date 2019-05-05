import json

# Load json from aces_data.json file
with open("../ACES/aces_data.json", "r") as file:
    aces_data = json.load(file)

# Load json from umd_data.json file
with open("../UMD/umd_data.json", "r") as file:
    umd_data = json.load(file)

# Check that ACES queries have been loaded
for key in aces_data.keys():
    print key

# Check that UMD queries have been loaded
for key in umd_data.keys():
    print key

# Quick test that ACES json was loaded and attributes can be accessed
print aces_data["ACES UMD"][0]["text"]
print aces_data["ACES UMD"][0]["country"]
print aces_data["ACES UMD"][0]["created_at"]

# Quick test that UMD json was loaded and attributes can be accessed
print umd_data["@UofMaryland"][0]["text"]
print umd_data["@UofMaryland"][0]["country"]
print umd_data["@UofMaryland"][0]["created_at"]
