# find the cv target in the image captuered by the display

import cv2
import numpy as np
import pyautogui
import time

#using my custom model, find the target in the image
def find_target():
    # load the model
    net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    
    # capture the screen
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        height, width, channels = frame.shape
        # detect the object
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward
