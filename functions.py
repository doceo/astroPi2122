# moduli utili al daynight
from random import randint
from orbit import ISS
from skyfield.api import load

# moduli utili al csv
import csv
from pathlib import Path
from time import sleep
from datetime import datetime, timedelta

from picamera import PiCamera

def capture(imName, test):
    if test:
        name_image = imName + ".jpg"
        camera = PiCamera()
        camera.resolution = (1296, 972)
        # Camera warm-up time
        sleep(2)
        camera.capture(f"{name_image}")


def dayNight(t):
    ephemeris = load('de421.bsp')
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


'''
QUELLO CHE SEGUE È LA PARTE CHE ANDREBBE INCLUSA IN MAIN.PY

'''

if __name__ == '__main__':
    #### ATTENZIONE, NEL MAIN VA CREATO UNA SOLA VOLTA ALTRIMENTI LO GENERA AD
    #### OGNI CICLO E LO SOVRASCRIVE SEMPRE
    # create_csv(data_file)

    ephemeris = load('de421.bsp')
    timescale = load.timescale()

    # Compute the coordinates of the Earth location directly beneath the ISS
    location = ISS.coordinates()

    base_folder = Path(__file__).parent.resolve()
    data_file = base_folder / 'data.csv'

    image_name = datetime.now().strftime("%Y%m%d-%H%M%S")
    path_image = str(base_folder) + "/" + image_name

    #  capture(path_image)

    row = (image_name, location.latitude.deg, location.longitude.deg, location.elevation.km)
    add_csv_data(data_file, row)
    print("file creato.\n")

    print("è giorno? ", dayNight())
