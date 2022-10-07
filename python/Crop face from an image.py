import cv2
import dlib
import numpy as np
from google.colab.patches import cv2_imshow
from scipy.spatial import distance

# use wget to download the file from 'https://github.com/italojs/facial-landmarks-recognition/raw/master/shape_predictor_68_face_landmarks.dat'

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


image = cv2.imread('IMAGE_PATH')
img = cv2.resize(image, (480, 480))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect the face
rects = detector(gray, 1)
# Detect landmarks for each face
for rect in rects:
  print(rect)
  x = rect.left()
  y = rect.top() #could be face.bottom() - not sure
  w = rect.right()
  h = rect.bottom() 

  area = image[y:h, x:w]
  cv2_imshow(area)

# Display the image
cv2_imshow(img)
# cv2_imshow(area)
