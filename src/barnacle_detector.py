import cv2
import numpy as np
import math
import os
from utils import save_image

class BarnacleDetector:

    def __init__(self, dp=1.2, minDist=20, param1=100, param2=25, minRadius=5, maxRadius=20, 
                 target_directory=None, draw_color=(255, 0, 0), draw_thickness=2):
        """
        Default values have been tuned to optimize for barnacle detection with the provided images
        """
        self.dp = dp
        self.minDist = minDist
        self.param1 = param1
        self.param2 = param2
        self.minRadius = minRadius
        self.maxRadius = maxRadius
        self.gaussian_size = 3
        self.sigmaX = 10

        self.target_directory = target_directory
        os.makedirs(self.target_directory, exist_ok=True)

        self.draw_color = draw_color # BGR colors
        self.draw_thickness = draw_thickness

    
    def detect(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (self.gaussian_size, self.gaussian_size), sigmaX=self.sigmaX)
        
        circles = cv2.HoughCircles(
            gray,
            cv2.HOUGH_GRADIENT,
            dp=self.dp,
            minDist=self.minDist,
            param1=self.param1,
            param2=self.param2,
            minRadius=self.minRadius,
            maxRadius=self.maxRadius
        )


        return self._remove_overlaps(np.round(circles[0]).astype(int)) if circles is not None else []

    def _remove_overlaps(self, circles):
        if len(circles) == 0:
            return []
        
        accepted = []
        for x, y, r in circles:
            if any(math.hypot(x - ax, y - ay) < (r + ar) for (ax, ay, ar) in accepted):
                continue
            accepted.append((x, y, r))
        
        return accepted


    def draw(self, image, circles):
        result = image.copy()

        for x, y, r in circles: 
            cv2.circle(result, (x, y), r, self.draw_color, self.draw_thickness)
        return result

    def save(self, image, path, log):
        name = f"barnacles_{os.path.basename(path)}"
        save_image(image, self.target_directory, name, log=log)
