import cv2
import numpy as np
from PIL import Image

class Glasses:
    def __init__(self, image) -> None:
        self.image = image
        self.edges = self._get_edges()

    @property       
    def debug_image(self):
        return Image.fromarray(self.edges)
    
    def worn(self):
        center = self.edges.T[(int(len(self.edges.T)/2))]
        return 255 in center
    
    def _get_edges(self):
        blurred = cv2.GaussianBlur(np.array(self.image),(3,3), sigmaX=0, sigmaY=0)
        return cv2.Canny(image=blurred, threshold1=100, threshold2=200)
        
