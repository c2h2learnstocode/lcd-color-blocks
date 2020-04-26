import cv2
import numpy as np  
import os
import random


img_width=600
img_height=480
block_size = 20
grid_size = 2

image = np.zeros((img_height, img_width,3), np.uint8)

for x in range(int(img_width/block_size)):
	for y in range(int(img_height/block_size)):
		x0 = x*block_size
		y0 = y*block_size
		x1 = x0 + block_size - grid_size
		y1 = y0 + block_size - grid_size
		color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		cv2.rectangle(image, (x0, y0), (x1, y1), color , -3)



cv2.imshow('image',image)
cv2.waitKey(0)
