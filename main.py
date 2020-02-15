import cv2
import numpy as np
import skimage.io as io
from FR import *
from SkinSegmentation import *

# frames reading
# function that calls (FR.py) functions that is used to inquire a filter cleared image of frame (preprossesing)
img = readFrame()
cv2.waitKey(0)
smoothed_img = smoothImg(img)
cv2.waitKey(0)
skin_mask = segmentSkin(smoothed_img)
cv2.waitKey(0)
skin_img = extractSkin(smoothed_img,skin_mask)
cv2.imshow('img', skin_img) 
cv2.waitKey(0)