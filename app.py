import cv2
import dlib
import numpy as np
from PIL import Image

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def get_landmarks(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    if len(rects) > 0:
        return np.array([[p.x, p.y] for p in predictor(gray, rects[0]).parts()])
    else:
        return None

def blend_faces(img1, img2):
    landmarks1 = get_landmarks(img1)
    landmarks2 = get_landmarks(img2)

    if landmarks1 is None or landmarks2 is None:
        print("Не удалось найти лица на одном из изображений.")
        return None

