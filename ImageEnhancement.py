# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 17:53:33 2021

@author: tmoha
"""

from PIL import Image,ImageEnhance

# import the image
image = Image.open("D:\Projects\ResearchProject\DirtImages\picture1.jpg")

# Adjust the colour
colourBalance = ImageEnhance.Color(image)
image = colourBalance.enhance(2)

# Sharpen the image
sharpenImage = ImageEnhance.Sharpness(image)
image = sharpenImage.enhance(2)

# Brightness Adjustments
brightImage = ImageEnhance.Brightness(image)
image = brightImage.enhance(1)

# Contrast Adjustments
contrastImage = ImageEnhance.Contrast(image)
image = contrastImage.enhance(1)

image.show()