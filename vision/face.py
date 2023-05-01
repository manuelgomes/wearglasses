import dlib
from pathlib import Path
from PIL import Image
import numpy as np

class Face:
    MARKS = [28,29,30,31,33,34,35]

    def __init__(self, model_path: Path, image: Image) -> None:
        self.detector = dlib.get_frontal_face_detector()
        print(model_path)
        self.predictor = dlib.shape_predictor(str(model_path))
        self.image = image

    @property
    def nose(self):
        res = self.detector(image=self.image)

        if len(res) == 0:
            return False
        else:
            return self._get_nose(res[0])
        
    def _get_nose(self, rect):
        landmarks = self._landmarks(rect)
        nose_bridge_x = [landmarks[i][0] for i in self.MARKS]
        x_min, x_max = min(nose_bridge_x), max(nose_bridge_x)
        y_min = landmarks[20][1]
        y_max = landmarks[31][1]
        shot = Image.fromarray(self.image)
        return shot.crop((x_min,y_min,x_max,y_max))

    def _landmarks(self, rect):
        return np.array([[p.x, p.y] for p in self.predictor(self.image, rect).parts()])
        
    

