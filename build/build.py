# build script for source images
# writes back to the original source data file so that we can keep cached
# images that were generated from links that no longer work

import json
import random
import urllib.request

from os.path import exists
from PIL import Image

lastSource = ""

def generate_new_cache_path():
    cachePath = "temp_image" # hack. we know it exists (we hope!!)
    while(exists(cachePath)):
        cachePath = "./output/cache/" \
            + str(random.randrange(100000000, 999999999)) \
            + ".png"
    return cachePath

def process_row(row, lastSource):
    # check if the url reaches a good image
    update = True
    if lastSource != row["original-source-link"]:
        try:
            urllib.request.urlretrieve(
                row["original-source-link"],
                "temp_image")
        except URLError as e:
            print("Relying on cached image segments for "
                + row["original-source-link"])
            update = False

    if update == True:
        lastSource = row["original-source-link"]
        
    #check if cache exists, if it doesnt and the link is dead, report an error
    cachePath = row["cached-image"]
    if (cachePath == "") or (exists(cachePath) == False):
        cachePath = generate_new_cache_path()
    
    if update == False:
        if exists(cachePath) == False:
            print("Error: no cache or valid link for source: " + row)
        else:
            print("Info: cached images exist "
                + "but the source is unavailable for: " + row)
        return
        
    imageSource = Image.open("temp_image")
    newImage = imageSource.crop((
        row["box"]["x"],
        row["box"]["y"],
        row["box"]["x"] + row["box"]["width"],
        row["box"]["y"] + row["box"]["height"]))
    newImage.save(cachePath, "PNG")
    row["cached-image"] = cachePath
    
    return

# start of script
dataPath = './source/sources.json';
if exists(dataPath) == False:
    sys.exit(-1)

dataFile = open(dataPath)
data = json.load(dataFile)
dataFile.close()

# now we have our list of sources in an object, process each one
for row in data:
    process_row(row, lastSource)

# update from local files.

# save back out
with open(dataPath, "w") as outFile:
    json.dump(data, outFile, indent=4)
