from picamera import *
import time

camera = PiCamera()
camera.start_preview()

while(1):
    for i in range(9):
    time.sleep(1800)
#	data = '{:>6.0f}'.format(time.monotonic())
	camera.capture('image/image%s.jpg' % i)
  
camera.stop_preview()