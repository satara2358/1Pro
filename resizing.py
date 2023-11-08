import os
import cv2

img = cv2.imread(os.path.join('.', 'bird.jpg'))

resizing_img= cv2.resize(img, (960, 540))

print(img.shape)
print(resizing_img)

cv2.imshow('img', img)
cv2.imshow('resizing_img', resizing_img)

cv2.waitKey(0)