import dlib
import cv2
import os

# Some constants
RESULT_PATH = './result/'       # The path that the result images will be saved
VIDEO_PATH = './dataset/'       # Dataset path
LOG_PATH = 'log.txt'            # The path for the working log file
# Face detector and landmark detector
face_detector = dlib.get_frontal_face_detector()   
landmark_detector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def shape_to_list(shape):
	coords = []
	for i in range(0, 68):
		coords.append((shape.part(i).x, shape.part(i).y))
	return coords

video_list = os.listdir(VIDEO_PATH)     # Read video list

for vid_name in video_list:
    vid = cv2.VideoCapture(VIDEO_PATH + vid_name)