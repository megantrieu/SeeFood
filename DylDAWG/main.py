import io
import os
import _tkinter

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
# file_name = os.path.abspath('hotdog1.jpg')
file_name = os.path.abspath('cat.jpeg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

is_hotdog = False
# print('Labels:')
for label in labels:
    # print(label.description)
    if label.description == "Hot dog":
        is_hotdog = True

if is_hotdog:
    print("Hot dog")
else:
    print("Not hot dog")
