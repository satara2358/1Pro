import os
import cv2

img = cv2.imread(os.path.join('.', 'data','logo.jpg' ))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rest, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
# segmentación de la imagen 
cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)