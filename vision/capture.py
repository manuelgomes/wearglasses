import cv2

class Capture:
    def __init__(self) -> None:
        self.camera = cv2.VideoCapture(0)

    def now(self):
        return self.camera.read()
