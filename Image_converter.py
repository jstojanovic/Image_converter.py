#!/usr/bin/env python
import os
from PIL import Image

directory = "images"

#avoids hidden directories
for filename in [f for f in os.listdir(directory) if not f.startswith('.')]:
    imageURL = os.path.join(directory, filename)
    
    img = Image.open(imageURL)
    #rotate by 90 degrees
    angle = 90
    img = img.rotate(angle)
    #resize to 128x128
    size = (128, 128)
    img = img.resize(size)
    #convert to jpeg
    img = img.convert("RGB")
    #save to ~/github/image_converter/converted_images/
    print(filename)
    img.save(os.path.join('/home/josip/github/image_converter/converted_images/', '{}.jpeg'.format(filename)))
