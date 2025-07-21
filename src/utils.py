from pathlib import Path
import cv2 

def save_image(image, target_dir, name, log=False):
    target = Path(target_dir)
    target.mkdir(parents=True, exist_ok=True)
    path = target / name
    # cv2.imwrite(str(path), image)
    success = cv2.imwrite(str(path), image)
    if log:     
        if success:
            print(f"\tWrote image to {path}")
        else:
            print(f"\tFailed to write image to {path}")
    return path