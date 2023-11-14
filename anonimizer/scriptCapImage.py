import cv2
import mediapipe as mp
import os

output_dir = './output'
if not os.path.exists(output_dir):
  os.makedirs(output_dir)

img_path = './data/logo.jpg'
img = cv2.imread(img_path)

H, W, _ = img.shape
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1, y1, w, h = int(bbox.xmin * W), int(bbox.ymin * H), int(bbox.width * W), int(bbox.height * H)

            # img = cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 5)
            img[y1:y1 + h, x1:x1 +w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (33, 33))

# save image 
cv2.imwrite(os.path.join(output_dir, 'out.png'), img)

# cv2.imshow('imgC', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
