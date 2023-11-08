import os
import cv2

img = cv2.imread(os.path.join('.','data', 'logo.jpg')) 

k=7
blur_imag= cv2.blur(img, (k,k))

cv2.imshow('img',img)
cv2.imshow('blur_img', blur_imag)
cv2.waitKey(0)