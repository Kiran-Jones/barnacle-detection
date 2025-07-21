import cv2
import numpy as np
import os
from pathlib import Path

from .image_loader import ImageLoader
from .utils import save_image

class FrameExtractor:
    def __init__(self, loader: ImageLoader, target_directory=None):
        self.target_directory = target_directory

        if self.target_directory is not None:
            os.makedirs(self.target_directory, exist_ok=True)

        self.loader = loader

        # hue range for barnacle detection in HSV color space
        # these values were determined by experimentation with the provided images
        self.lower_hue = np.array([50, 20, 20])
        self.upper_hue = np.array([100, 255, 255])

        self.frames = []
        

    def extract(self):
        for image_path in self.loader.images:

            image = cv2.imread(image_path, cv2.IMREAD_COLOR)
            if image is None:
                raise FileNotFoundError(f"Could not load {image_path}")
            
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.lower_hue, self.upper_hue)

            # 2) Clean up small gaps in the frame
            b, g, r = cv2.split(image)
            mask[r >= g] = 0
            mask[r >= b] = 0

            h, w = mask.shape
            flooded = cv2.floodFill(mask.copy(), None, (w//2, h//2), 100)[1]

            # make a 3‐channel version of the flood region
            flood_region = (flooded == 100)  # boolean mask
            
            # zero everything outside the flood region
            result = image.copy()
            result[~flood_region] = 0

            if self.target_directory is not None:
                stem = Path(image_path).stem
                suffix = Path(image_path).suffix
                name = f"frame_{stem}{suffix}"
                save_image(result, self.target_directory, name)

            self.frames.append((result, image_path))
        return self.frames
