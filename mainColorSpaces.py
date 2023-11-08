import os
import cv2

img = cv2.imread(os.path.join('.','data', 'logo.jpg')) 

# img_crop = img[220:640, 320:840]
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow('img_gray', img_gray)
cv2.imshow('img_rgb', img_rgb)
cv2.waitKey(0)
