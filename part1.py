import numpy as np
from scipy import ndimage
from PIL import Image,ImageFilter
import cv2

#apply the gaussian blur using the built-in function in python
def smooth_image(photo):
    blurred_photo=photo.filter(ImageFilter.GaussianBlur) 
    return blurred_photo

#compute the gradient magnitude and output the gradient intensity picture
def gradient_magnitude(blurred_photo):
# Below code converts image gradient in both x and y direction
    lap = cv2.Laplacian(blurred_photo,cv2.CV_64F,ksize=3) 
    lap = np.uint8(np.absolute(lap))

# Below code convert image gradient in x direction
    sobelx= cv2.Sobel(blurred_photo,0, dx=1,dy=0)
    sobelx= np.uint8(np.absolute(sobelx))

# Below code convert image gradient in y direction
    sobely= cv2.Sobel(blurred_photo,0, dx=0,dy=1)
    sobely = np.uint8(np.absolute(sobely))
    results = [lap,sobelx,sobely]
    images =["Gradient Image","Gradient In X direction","Gradient In Y direction"]

    for i in range(3):
        Gradient_Image=plt.figure(1)
        plt.title(results[i])
        plt.subplot(1,3,i+1)
        plt.imshow(results[i],"plasma")
        plt.xticks([])
        plt.yticks([])
    
    return Gradient_Image