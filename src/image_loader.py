import cv2
import numpy as np
import os


class ImageLoader:
    def __init__(self, directory_path=None):
        if directory_path:
            if not os.path.isdir(directory_path):
                os.makedirs(directory_path, exist_ok=True)
            self.directory_path = directory_path
        else:
            raise ValueError("You must provide a directory_path.")
        
        self.images = []
        self._load_images()

    def _load_images(self): 
        """Load images from the specified directory."""
        if not self.directory_path:
            raise ValueError("No directory path provided for loading images.")

        images = []
        for filename in os.listdir(self.directory_path):
            valid_extensions = ('.png', '.jpg', '.jpeg')
            if filename.endswith(valid_extensions):
                image_path = os.path.join(self.directory_path, filename)
                images.append(image_path)
        if not images:
            raise FileNotFoundError(f"No valid images found in {self.directory_path}")
        self.images = images
