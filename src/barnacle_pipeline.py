from image_loader import ImageLoader 
from frame_extractor import FrameExtractor
from barnacle_detector import BarnacleDetector

class BarnaclePipeline:

    def __init__(self, input_image_directory="data", output_image_directory="outputs", frame_image_directory=None, log=False):
        self.input_image_directory = input_image_directory
        self.output_image_directory = output_image_directory
        self.frame_image_directory = frame_image_directory
        self.log = log

        self.loader = ImageLoader(directory_path=self.input_image_directory)
        self.extractor = FrameExtractor(loader=self.loader, target_directory=self.frame_image_directory)
        self.detector = BarnacleDetector(target_directory=self.output_image_directory)
    
    def run(self):
        for frame, path in self.extractor.extract():
            circles = self.detector.detect(frame)
            if self.log:
                print(f"Detected {len(circles)} barnacles in {path}")
            image = self.detector.draw(frame, circles)
            self.detector.save(image, path, self.log)
        
        print(f"\n\nDetected barnacle images written to folder '{self.output_image_directory}'")

        

    