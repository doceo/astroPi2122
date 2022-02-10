from picamera import PiCamera
from time import sleep
from datetime import datetime, timedelta
from pathlib import Path

def capture(imName, test):
    if test:
        name_image = imName + ".jpg"
        camera = PiCamera()
        camera.resolution = (1296, 972)
        # Camera warm-up time
        sleep(2)
        camera.capture(f"{name_image}")


base_folder = Path(__file__).parent.resolve()
image_name = datetime.now().strftime("%Y%m%d-%H%M%S")
path_image = str(base_folder) + "/" + image_name
capture(path_image, 0)
