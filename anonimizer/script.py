import cv2
import mediapipe as mp

img_path = './data/logo.jpg'
img = cv2.imread(img_path)

mp_fdtc = mp.solutions.face_detection

with mp_fdtc.FaceDetection( model_selection=0, min_detection_confidence=0.5 ) as  face_detection:
  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  out = face_detection.process(img_rgb)
  
  print(out.detections)