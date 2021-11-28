#libraries
import numpy as np
from PIL import Image
import scipy as sp
import matplotlib as plt
import part1.py #Gabby, smooth_image and gradient_map
import part2.py #Chris, suppress_nommaxima, double_threshold
#intake photo
photopath = "path/to/photo"
newphotopath = photopath[:-4]+"_greyscale"+photopath[-4:]
init_img = Image.open(photopath).convert('L')
init_img.save(newphotopath)
img = Image.open(newphotopath) #This is the initial greyscaled image

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
