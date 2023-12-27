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

print(f"Source folder: {sourceFolder} \nImage format: {imageFormat}")

image_paths = []

for filename in os.listdir(sourceFolder):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        image_path = os.path.join(sourceFolder, filename)
        image_paths.append(image_path)

for path in image_paths:
    pullface(path, imageFormat, outputFolder)
