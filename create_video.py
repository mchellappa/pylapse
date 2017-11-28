#!/usr/local/bin/python3

import cv2
import argparse
import os

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ext", "--extension", required=False, default='png', help="extension name. default is 'png'.")
ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
args = vars(ap.parse_args())

# Arguments
dir_path = "c:/Users/muthu/Pictures/Day07/"
ext = args['extension']
output = args['output']
print dir_path
images = []
for f in os.listdir(dir_path):
    if f.endswith(ext):
        images.append(f)

# Determine the width and height from the first image

image_path = os.path.join(dir_path, images[0])

frame = cv2.imread(image_path)
#cv2.imshow('video',frame)
height, width, channels = frame.shape

size = (width,height)

fps = 20

fourcc = cv2.cv.CV_FOURCC(*'MJPG') # note the lower case
vout = cv2.VideoCapture(0)
#success = vout.open('output.avi', fourcc, 20.0, (640,480))
vout = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))




for image in images:

    image_path = os.path.join(dir_path, image)
    frame = cv2.imread(image_path)

    resize = cv2.resize(frame, (640, 480))
    
    vout.write(resize ) 

    cv2.imshow('frame', resize)
  
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break

# Release everything if job is finished
vout.release()
cv2.destroyAllWindows()

print("The output video is {}".format(output))