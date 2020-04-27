import cv2
import numpy as np  
import os
import random


img_width=600
img_height=480
block_size = 20
grid_size = 2

image = np.zeros((img_height, img_width,3), np.uint8)


def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)



x_blocks= int(img_width / block_size)
y_blocks= int(img_height/ block_size)



for x in range(int(img_width/block_size)):
    for y in range(int(img_height/block_size)):
        x0 = x*block_size
        y0 = y*block_size
        x1 = x0 + block_size - grid_size
        y1 = y0 + block_size - grid_size
        
        cart_x = x-x_blocks/2
        cart_y = y-y_blocks/2
        r, theta = cart2pol(cart_x,cart_y)
        if r>img_height/block_size/2+1:
            #outside the polar
            color=(0,0,0)
        else:
            theta_normalized = (theta/np.pi + 1)/2
            r_col = 255-int( (r / (img_height/block_size/2+1))*255)
            #print(r, theta_normalized)
            if theta_normalized < 1/3:
                color = (int(theta_normalized*255), r_col, r_col)
            elif theta_normalized < 2/3:
                color = (r_col, int((theta_normalized-1/3)*255), r_col)
            else:
                color = (r_col, r_col, int((theta_normalized-2/3)*255))

        cv2.rectangle(image, (x0, y0), (x1, y1), color , -3)

cv2.imwrite("polar_lcdtest.png", image)

cv2.imshow('image',image)
cv2.waitKey(0)


for x in range(int(img_width/block_size)):
    for y in range(int(img_height/block_size)):
        x0 = x*block_size
        y0 = y*block_size
        x1 = x0 + block_size - grid_size
        y1 = y0 + block_size - grid_size
        
        cart_x = x-x_blocks/2
        cart_y = y-y_blocks/2
        r, theta = cart2pol(cart_x,cart_y)
        if r>img_height/block_size/2+1:
            #outside the polar
            color=(0,0,0)
        else:
            color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        cv2.rectangle(image, (x0, y0), (x1, y1), color , -3)

cv2.imwrite("random_lcdtest.png", image)

cv2.imshow('image',image)
cv2.waitKey(0)
