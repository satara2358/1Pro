import os 
import cv2
import numpy as np


img = cv2.imread(os.path.join('.', 'data', 'logo.jpg'))
img_edge = cv2.Canny(img, 100,200)

cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.waitKey(0)