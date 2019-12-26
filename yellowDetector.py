import cv2
from helper import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
from pipeline import process_image, LaneMemory

#reading in an image
image = mpimg.imread('newImage.jpg')

plt.imshow(image)  # if you wanted to show a single color channel image called 'gray', 
                   
gray_img = grayscale(image)
    
darkened_img = adjust_gamma(gray_img, 0.5)
 
yellow_mask = isolate_color_mask(to_hls(image), np.array([10, 0, 100], dtype=np.uint8), np.array([40, 255, 255], dtype=np.uint8))

masked_img = cv2.bitwise_and(darkened_img, darkened_img, mask=yellow_mask)
    
blurred_img = gaussian_blur(masked_img, kernel_size=7)
    
canny_img = canny(blurred_img, low_threshold=70, high_threshold=140)
    
hough_lines_imgs = []

lines = get_hough_lines(canny_img)

hough_lines_imgs.append(draw_lines(image, lines))

plt.imshow(image)
