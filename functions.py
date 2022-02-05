# moduli utili al daynight
from random import randint
from orbit import ISS
from skyfield.api import load

# moduli utili al csv
import csv
from pathlib import Path
from time import sleep
from datetime import datetime, timedelta

# moduli utili al ndvi
import cv2
import numpy as np
from fastiecm import fastiecm


def capture(imName):
    name_image = imName + ".jpg"
    camera = PiCamera()
    camera.resolution = (1296, 972)
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


def display(image, image_name):
    image = np.array(image, dtype=float) / float(255)
    shape = image.shape
    height = int(shape[0] / 2)
    width = int(shape[1] / 2)
    image = cv2.resize(image, (width, height))
    cv2.namedWindow(image_name)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)
    out_min = 0.0
    out_max = 255.0
    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min
    return out


def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom == 0] = 0.01
    ndvi = (b.astype(float) - r) / bottom
    return ndvi


def contrast(image):
    display(image, 'Original')
    contrasted = contrast_stretch(image)
    display(contrasted, 'Contrasted original')
    cv2.imwrite('contrasted.png', contrasted)
    return contrasted


def contrastNdvi(contrasted):
    ndvi = calc_ndvi(contrasted)
    display(ndvi, 'NDVI')
    ndvi_contrasted = contrast_stretch(ndvi)
    cv2.imwrite('ndvi_contrasted.png', ndvi_contrasted)
    display(ndvi_contrasted, 'NDVI contrasted')
    return ndvi_contrasted


def colorMapping(ndvi_contrasted):
    color_mapped_prep = ndvi_contrasted.astype(np.uint8)
    color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
    display(color_mapped_image, 'Color mapped')
    cv2.imwrite('color_mapped_image.png', color_mapped_image)
    return color_mapped_image


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

    row = (image_name, location.latitude, location.longitude, location.elevation.km)
    add_csv_data(data_file, row)
    print("file creato.\n")

    print("è giorno? ", dayNight())
