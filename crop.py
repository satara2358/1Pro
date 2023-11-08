import os
import cv2

img = cv2.imread(os.path.join('.', 'bird.jpg')) 
print(img.shape)

img_crop = img[320:640, 420:840]

cv2.imshow('img', img)
cv2.imshow('img_crop', img_crop)
cv2.waitKey(0)
