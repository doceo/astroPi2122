from time import sleep
from picamera import PiCamera
from pathlib import Path
from time import time
from datetime import datetime, timedelta


def capture():
    
    base_folder = Path(__file__).parent.resolve()
    image_name = datetime.now().strftime("%Y%m%d-%H%M%S")
    path_image = str(base_folder) + "/" + image_name
    camera = PiCamera()
    camera.resolution = (1296,972)
    # Camera warm-up time
    sleep(2)
    camera.capture(f"{image_name}")

capture()

