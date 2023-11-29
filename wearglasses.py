#!/home/manuel/.virtualenvs/wearglasses-oxjq/bin/python
from pathlib import Path
import os
from runlog.recorder import Recorder
from runlog.reaper import Reaper
from vision.face import Face
from vision.capture import Capture
from discriminator.glasses import Glasses
from action.notification import Notification

BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))

rec = Recorder(basedir=BASE_DIR)
ok, image = Capture().now()

if not ok:
    rec.tell("NOPIC")
    raise IOError("No image found")

model = Face(
    BASE_DIR.joinpath("assets", "shape_predictor_68_face_landmarks.dat"), image
)
nose = model.nose
rec.save(nose, "nose")

discriminator = Glasses(nose)
rec.save(discriminator.debug_image, "edges")
present = discriminator.worn()

if present:
    rec.tell("PRESENT")
else:
    rec.tell("ABSENT")
    note = Notification()
    note.display("Coder")

runsdir = BASE_DIR.joinpath("runs")
man = Reaper(path=runsdir)
man.check()
