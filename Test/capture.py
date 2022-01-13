from time import sleep
from picamera import PiCamera
from pathlib import Path

def capture():
    base_folder = Path(__file__).parent.resolve()
    camera = PiCamera()
    camera.resolution = (1296,972)
    # Camera warm-up time
    sleep(2)
    camera.capture(f"{base_folder}/datatime.now.jpg")