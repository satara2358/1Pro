import os 
import cv2
import numpy as np

img = cv2.imread(os.path.join('.', 'data', 'logo.jpg'))
img_edge = cv2.Canny(img, 100,200)

img_edage_d = cv2.dilate(img_edge, np.ones((3,3), dtype=np.int8))

# texto
cv2.putText(img, 'B2', (600,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,0),4)

cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edage_d)
cv2.waitKey(0)

