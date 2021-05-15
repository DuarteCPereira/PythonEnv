import cv2
import yaml
import numpy as np
import math
from matplotlib import pyplot as plt
import vidProc


'''
img = cv2.imread('girdImage2.jpg')
frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(frame_gray,100,250,cv2.THRESH_BINARY_INV)


lines = vidProc.binaryGridDetection(img)
dir1,dir2 = vidProc.finddirs(lines)
intersectionPoints = vidProc.findIntPoints(binary,img)

'''
def main():
    windowName = "Preview"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False


    while ret:
    
        ret, frame = cap.read()
        
        #lines,cimg=vidProc.binaryGridDetection(frame)
        #intersectionPoints,cimg = vidProc.findIntPoints(frame)
        cimg = vidProc.findCircles(frame)
        cv2.imshow("frame", frame)
        cv2.imshow(windowName, cimg)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    cap.release()
    
main()