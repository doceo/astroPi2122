from time import sleep
from picamera import PiCamera
from pathlib import Path
from time import time

def capture():
    
    base_folder = Path(__file__).parent.resolve()
    name_image = str(base_folder) + "/images/" + str(time()) +".jpg"
    camera = PiCamera()
    camera.resolution = (1296,972)
    # Camera warm-up time
    sleep(2)
    camera.capture(f"{name_image}")

if __name__ == "__main__":

    capture()

