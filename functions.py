from random import randint
from orbit import ISS
from skyfield.api import load

import csv
from pathlib import Path
from time import sleep
from datetime import datetime, timedelta


ephemeris = load('de421.bsp')
timescale = load.timescale()

# Compute the coordinates of the Earth location directly beneath the ISS
location = ISS.coordinates() 

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
    print(funcTest())
