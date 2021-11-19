#libraries
import numpy as np
from PIL import Image, ImageFilter
import imageio
import scipy as sp
import matplotlib.pyplot as plt
import visvis as vv
import cv2 as cv
import part1 #Gabby, smooth_image and gradient_map
#import part2.py #Chris, suppress_nommaxima, double_threshold


#intake photo
photopath = "./images/testimg.png"
newphotopath = photopath[:-4]+"_greyscale"+photopath[-4:]
init_img = Image.open(photopath).convert('L')
init_img.save(newphotopath)
img = imageio.imread(newphotopath) #This is the initial greyscaled image

part1 = gradient_magnitude(smooth_image(img))

#imgplot2 = plt.imshow(part1)

#def suppress_nonmaxima():
# Apply nonmaxima suppression to the gradient magnitude


#def double_threshold():
# Use double thresholding to detect and link edges
# mask1 = input photo < theshold1
# mask2 = input_photo < theshold2




#check our work with python functions that use canny edge detection algorithm
#img = cv.imread('img',0)
#edges = cv.Canny(img,100,200)
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#plt.show()
