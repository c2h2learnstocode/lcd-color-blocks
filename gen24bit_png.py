import cv2
import numpy as np  
import os
import random


img_width=800
img_height=480


vals=[0, 2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 255]

for val in vals:
    image = np.full((img_height, img_width,3), val, dtype=np.uint8)
    print(image)
    #cv2.imshow('image',image)
    #cv2.waitKey(0)
    cv2.imwrite("uniform_"+str(val)+"_lcdtest.png", image)
