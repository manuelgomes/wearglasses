#!/usr/bin/env python
import datetime
import sys
from pathlib import Path

import cv2
import dlib
import numpy as np
from PIL import Image
from rich import print
import gi
gi.require_version("Notify", "0.7")
from gi.repository import Notify

from runlog.recorder import Recorder
rec = Recorder()

cam = cv2.VideoCapture(0)
result, image = cam.read()
if not result:
    rec.tell("NOPIC")
    raise IOError("No image found")

shot = Image.fromarray(image)
rec.save(shot, "shot")


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./assets/shape_predictor_68_face_landmarks.dat')
detected = detector(image)

if len(detected) == 0:
    rec.tell("NOFACE")
    sys.exit(0)

rect = detected[0]
sp = predictor(image, rect)
landmarks = np.array([[p.x, p.y] for p in sp.parts()])

nose_bridge_x = []
nose_bridge_y = []

for i in [28,29,30,31,33,34,35]:
    nose_bridge_x.append(landmarks[i][0])
    nose_bridge_y.append(landmarks[i][1])

### x_min and x_max
x_min = min(nose_bridge_x)
x_max = max(nose_bridge_x)
### ymin (from top eyebrow coordinate),  ymax
y_min = landmarks[20][1]
y_max = landmarks[31][1]

area = shot.crop((x_min,y_min,x_max,y_max))
rec.save(area, "area")

img_blur = cv2.GaussianBlur(np.array(area),(3,3), sigmaX=0, sigmaY=0)
edges = cv2.Canny(image =img_blur, threshold1=100, threshold2=200)
edges_center = edges.T[(int(len(edges.T)/2))]

rec.save(Image.fromarray(edges), "edges")

present =  255 in edges_center
print(present)
if present:
    rec.tell("PRESENT")
else:
    rec.tell("ABSENT")
    Notify.init("Wear Glasses")
    notification=Notify.Notification.new ("Wear Glasses",
                               "Put on your glasses, Manny!",
                               "dialog-information")
    notification.set_timeout(0)
    notification.show()

