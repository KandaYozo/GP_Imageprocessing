import cv2
import numpy as np
import skimage.io as io
#----------------------------------------------------------------------------
# function used to read a frame from file
# input: none
# output: image
def readFrame():
    img = cv2.imread('C:/Users/Hambart/Desktop/GP/DataSet-Trial/close.png')
    cv2.imshow('img', img)
    return img
#----------------------------------------------------------------------------
# function used to smooth from image
# input: image
# output: image
def smoothImg(img):
    blur = cv2.bilateralFilter(img,9,75,75)
    cv2.imshow('blur', blur)
    return blur
#----------------------------------------------------------------------------
# function used to sharp edges from image
# input: image
# output: image
def sharpenEdges(img):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpend = cv2.filter2D(img, -1, kernel)
    cv2.imshow('sharped', sharpend)
    return sharpend

