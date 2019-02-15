# Take JSON file, import select records, store in MongoDB
import json
from pymongo import MongoClient
import urllib.request

# Initialize Database
client = MongoClient() # Initialize Mongo Client
power_db = client['power_db'] # Reference Client, create Power
power = power_db['power']
    
# Import EBA data
incoming = []
i = 0
with open('Data/EBA.json') as file:
    for line in file:
        if i < 644
            incoming.append(json.loads(line))
            i += 1
        else:
            break

power.insert_many(incoming);  

# Import Manifest
with urllib.request.urlopen("http://api.eia.gov/bulk/manifest.txt") as url:
    manifest = json.loads(url.read().decode())

power_db['manifest'].insert_one(manifest)
