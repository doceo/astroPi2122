
# moduli utili al daynight
from random import randint
from orbit import ISS
from skyfield.api import load

# moduli utili al csv
import csv
from pathlib import Path
from time import sleep
from datetime import datetime, timedelta

# moduli utili all'acquisizione immagine
from picamera import PiCamera
from time import time

def capture(imName):
    
    name_image = imName +".jpg"
    camera = PiCamera()
    camera.resolution = (1296,972)
    # Camera warm-up time
    sleep(2)
    camera.capture(f"{name_image}")


def dayNight():
    t = timescale.now()
    if ISS.at(t).is_sunlit(ephemeris):
        return True
    else:
        return False

# Define the function that create the CSV and write the firts row
def create_csv(data_file):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time", "Latitude", "Longitude", "Elevation")
        writer.writerow(header)

# Define the function to write the other row with the values
def add_csv_data(data_file, data):
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)




if __name__ == '__main__':


    ephemeris = load('de421.bsp')
    timescale = load.timescale()

    # Compute the coordinates of the Earth location directly beneath the ISS
    location = ISS.coordinates() 

    base_folder = Path(__file__).parent.resolve()
    data_file = base_folder/'data.csv'

    image_name = str(time())
    path_image = base_folder + "/" + image_name

    capture(path_image)

    create_csv(data_file)

    row = (image_name, location.latitude, location.longitude, location.elevation.km)
    add_csv_data(data_file, row)
    print("file creato.\n")

    print("è giorno? ", dayNight())
