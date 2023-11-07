import os
import cv2

imge_path = os.path.join('.', 'data', 'bird.jpg')
img = cv2.imread(imge_path)


cv2.imwrite(os.path.join('.', 'data', 'bird_out.jpg'), img)
cv2.imshow('image', img)
cv2.waitKey(0)   