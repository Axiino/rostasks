#importing some useful packages
import cv2
from helper import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
from pipeline import process_image, LaneMemory

#reading in an image
image = mpimg.imread('newImage.jpg')

# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#printing out some stats and plotting
print('This image is:', type(image), 'with dimensions:', image.shape)
plt.imshow(image)  # if you wanted to show a single color channel image called 'gray', 
# for example, call as plt.imshow(gray, cmap='gray')
                   
gray_imgs = [grayscale(img) for img in img_list]
#display_imgs(gray_imgs, test_imgs) НЕ СРАБОТАЛО
# save_imgs(gray_imgs, test_imgs, prefix="Gray")
for img in gray_imgs:
    plt.imshow(img)
    
    
darkened_imgs = [adjust_gamma(img, 0.5) for img in gray_imgs]

for img in darkened_imgs:
    plt.imshow(img)
    
white_masks = []
yellow_masks = []
white_masks = [isolate_color_mask(to_hls(img), np.array([0, 200, 0], dtype=np.uint8), np.array([200, 255, 255], dtype=np.uint8)) for img in img_list]
yellow_masks = [isolate_color_mask(to_hls(img), np.array([10, 0, 100], dtype=np.uint8), np.array([40, 255, 255], dtype=np.uint8)) for img in img_list]
masked_imgs = []
for i in range(len(img_list)):
#     mask = cv2.bitwise_or(white_masks[i], yellow_masks[i])
    masked_imgs.append(cv2.bitwise_and(darkened_imgs[i], darkened_imgs[i], mask=yellow_masks[i]))
    
for img in masked_imgs:
    plt.imshow(img)
    
blurred_imgs = [gaussian_blur(img, kernel_size=7) for img in masked_imgs]
# display_imgs(blurred_imgs, test_imgs)
# save_imgs(blurred_imgs, test_imgs, prefix='Gaussian')
for img in blurred_imgs:
    plt.imshow(img)
    
canny_imgs = [canny(img, low_threshold=70, high_threshold=140) for img in blurred_imgs]
# display_imgs(canny_imgs, test_imgs)
# save_imgs(canny_imgs, test_imgs, prefix='Canny')
for img in canny_imgs:
    plt.imshow(img)
    
    
hough_lines_imgs_canny = []
lines_canny = []
for img in canny_imgs:
    lines_canny.append(get_hough_lines(img))
    
for img, line in zip(img_list, lines_canny):
    hough_lines_imgs_canny.append(draw_lines(img, line))
    
for img in hough_lines_imgs_canny:
    plt.imshow(img)
# display_imgs(hough_lines_imgs_canny, test_imgs)
# save_imgs(hough_lines_imgs_canny, test_imgs, prefix='Hough')
