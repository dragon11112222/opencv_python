import cv2
import sys

cap = cv2.VideoCapture('data/woman.mp4')

if not cap.isOpened():
    print('video open failed!')
    sys.exit()