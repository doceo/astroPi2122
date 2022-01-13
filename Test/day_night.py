"""The Sense HAT documentation contains sections on how to retrieve data from the environmental sensors (temperature,
humidity, pressure) and the Inertial Measurement Unit (IMU) (acceleration, orientiation). Additional documentation is
available for interacting with the light and colour sensor. You can also explore the wide range of Sense HAT projects
available from the Raspberry Pi Foundation. Through Sense HAT we can detect if the camera is framing a dark or
illuminated part of the earth."""

from sense_hat import SenseHat

sense = SenseHat()
sense.color.gain = 16
light = sense.color.clear
if light < 64:
    print('Dark')
else:
    print('Light')
