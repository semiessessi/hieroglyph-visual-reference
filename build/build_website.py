# build script for website stuff that isn't the cached images

import json

from os.path import exists

# start of script
dataPath = './source/sources.json';
if exists(dataPath) == False:
    sys.exit(-1)

dataFile = open(dataPath)
data = json.load(dataFile)
dataFile.close()

# build a map from gardiner codes to lists of structured data
imageDataLookup = {}

for row in data:
    # process_row(row, lastSource)
    if row["glyph"] not in imageDataLookup:
        imageDataLookup[row["glyph"]] = []
    imageDataLookup[row["glyph"]].append(row)

lookupData = "const imageDataLookup = new Map([\n";
for glyphKey in imageDataLookup:
    lookupData += '\t["' + glyphKey + '",\n\t\t[\n'
    rows = imageDataLookup[glyphKey]
    for row in rows:
        lookupData += '\t\t\t{\n'
        lookupData += '\t\t\t\tglyph: "' + glyphKey + '",\n'
        lookupData += '\t\t\t\tsourceURL: "' + row["original-source-link"] + '",\n'
        lookupData += '\t\t\t\tsourceName: "' + row["source-name"] + '",\n'
        lookupData += '\t\t\t\tsourceLocation: "' + row["origin-location"] + '",\n'
        lookupData += '\t\t\t\tsourceDynasty: "' + str(row["dynasty"]) + '",\n'
        lookupData += '\t\t\t\tlicense: "' + row["license"] + '",\n'
        lookupData += '\t\t\t\tcredit: "' + row["credit"] + '",\n'
        lookupData += '\t\t\t\timageURL: "' + row["cached-image"] + '"\n'
        lookupData += '\t\t\t},\n'
    # kill last comma
    lookupData = lookupData[:-2] + '\n'
    lookupData += '\t\t]\n\t],\n'
# kill last comma
lookupData = lookupData[:-2] + '\n'
lookupData += "]);\n";

# write the file out with the lookup table
lookupPath = './scripts/imageDataLookup.js'
lookupFile = open(lookupPath, 'w')
lookupFile.write(lookupData)
lookupFile.close()
