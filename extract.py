import os
import json

from facepuller import pullface

with open('inputs.json', 'r') as file:
    data = json.load(file)

sourceFolder = data["sourceFolder"]
imageFormat = data["imageFormat"]
outputFolder = f"{sourceFolder}_faces"

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

print(f"Source folder: {sourceFolder} \n Image format: {imageFormat}")

image_paths = []

for filename in os.listdir(sourceFolder):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        print("yay")
        image_path = os.path.join(sourceFolder, filename)
        image_paths.append(image_path)
    else:
        print("nope")

print(image_paths)

for path in image_paths:
    pullface(path, imageFormat, outputFolder)
