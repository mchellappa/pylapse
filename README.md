Pylapse
=======


Create timelapse using opencv,ffmpeg and python

Usage :
* to see a preview of the camera that you set to take the timelapse:
> python pylapse.py --preview True


* to start a timelapse :
> python pylapse.py -t True

for more help do python pylapse.py -h
```
Usage: pylapse.py [options]

Options:
  -h, --help            show this help message and exit
  -p PREVIEW, --preview=PREVIEW
                        Preview the camera
  -t TIMELAPSE, --timelapse=TIMELAPSE
                        start taking pictures for the timelapse
  -w WIDTH, --width=WIDTH
                        camera image width in pixels
  -l HEIGHT, --height=HEIGHT
                        camera image height in pixels
  -c CAM_IDX, --cam_idx=CAM_IDX
                        camera index
  -f FPS, --fps=FPS     video output fps
  -v VIDEO_DURATION, --video-duration=VIDEO_DURATION
                        output video duration
  -e EVENT_DURATION, --event-duration=EVENT_DURATION
                        event duration (how much time the event is going to
                        take)
  -o OUTPUT_DIR, --output-dir=OUTPUT_DIR
                        the folder it would create the images and the video
  -q QUALITY, --quality=QUALITY
                        image quality of the compression

```
notes:
- for now it uses opencv to get the images from the camera
- Please copy opencv from source forge and copy cv2 to python folder. It is supported only on python2x
- Please use "create_video.py -ext JPG -o output.mp4" to create the video (Other codecs in fourcc does not work and this is the one which worked on my windows machine)
- Select the default option in the window to generate a compressed file
