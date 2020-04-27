import cv2
import numpy as np  
import os
import random


img_width=800
img_height=480


vals=[0, 2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 255]

#R
for val in vals:
    vec=(0, 0, val)
    image = np.full((img_height, img_width,3), vec)
    cv2.imwrite("uniform_R"+str(val)+"_lcdtest.png", image)
  
#G
for val in vals:
    vec=(0, val, 0)
    image = np.full((img_height, img_width,3), vec)
    cv2.imwrite("uniform_G"+str(val)+"_lcdtest.png", image)

#B
for val in vals:
    vec=(val, 0, 0)
    image = np.full((img_height, img_width,3), vec)
    cv2.imwrite("uniform_B"+str(val)+"_lcdtest.png", image)