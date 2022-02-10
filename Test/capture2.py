from picamera import PiCamera
from pathlib import Path
base_folder = Path(__file__).parent.resolve()
def capture(camera, image):
    camera.capture(image)
cam = PiCamera
cam.resolution = (1296, 972)
counter = 1
image_file = f"{base_folder}/photo_{counter:03d}.jpg"
capture(cam, image_file)