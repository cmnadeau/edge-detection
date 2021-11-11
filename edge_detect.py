#libraries
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import part1.py #Gabby, smooth_image and gradient_map
import part2.py #Chris, suppress_nommaxima, double_threshold
#intake photo
# greyscale
def rgb2grey(rgbimg):
  return np.dot(rgbimg[...,:3],[0.2989, 0.5870, 0.1140])

def smooth_image(photo):  
#Smooth image with Gaussian filter (using built-in fn


def gradient_magnitude():
 # Compute gradient magnitude and orientation w/ finite-diff approx. for partials
def suppress_nonmaxima():
# Apply nonmaxima suppression to the gradient magnitude


def double_threshold():
# Use double thresholding to detect and link edges
# mask1 = input photo < theshold1
# mask2 = input_photo < theshold2
