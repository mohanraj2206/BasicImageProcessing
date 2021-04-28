# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 22:40:37 2021

@author: tmoha
"""

from PIL import Image,ImageFilter

# import the image
image = Image.open("D:\Projects\ResearchProject\DirtImages\picture1.jpg")

# Apply edge enhancement filter
edgeEnahnced = image.filter(ImageFilter.EDGE_ENHANCE)

# Apply increased edge enhancement filter
moreEdgeEnahnced = image.filter(ImageFilter.EDGE_ENHANCE_MORE)

# Show original image - before applying edge enhancement filters
image.show() 

# Show image - after applying edge enhancement filter
edgeEnahnced.show()

# Show image - after applying increased edge enhancement filter
moreEdgeEnahnced.show()