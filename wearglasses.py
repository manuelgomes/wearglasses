#!/usr/bin/env python
from pathlib import Path

from runlog.recorder import Recorder
from vision.face import Face
from vision.capture import Capture
from discriminator.glasses import Glasses
from action.notification import Notification

rec = Recorder()
ok, image = Capture().now()

if not ok:
    rec.tell("NOPIC")
    raise IOError("No image found")

model = Face(
    Path.cwd().joinpath("assets", "shape_predictor_68_face_landmarks.dat"), 
    image
)
nose = model.nose
rec.save(nose, "nose")

discriminator = Glasses(nose)
rec.save(discriminator.debug_image, "edges")
present = discriminator.worn()

print(present)
if present:
    rec.tell("PRESENT")
else:
    rec.tell("ABSENT")
    note = Notification()
    note.display("Manny")

