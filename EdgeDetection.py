# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 22:53:43 2021

@author: tmoha
"""

import cv2
from matplotlib import pyplot as plt

# Read image
img = cv2.imread("D:\Projects\ResearchProject\DirtImages\picture1.jpg",0)

# Apply Canny Edge Detection
edges = cv2.Canny(img,100,200)

plt.subplot(121)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()