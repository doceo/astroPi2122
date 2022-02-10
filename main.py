# MODULI PERSONALI
from functions import *

# MODULI PER CSV
import csv
from orbit import ISS

from pathlib import Path
from time import sleep
from datetime import datetime, timedelta

# MODULI PER PICAMERA
from picamera import PiCamera
from time import time



'''
descrizioni variabili globali
'''
ephemeris = load('de421.bsp')
timescale = load.timescale()

image_name = datetime.now().strftime("%Y%m%d-%H%M%S")
path_image = str(base_folder) + "/" + image_name

light = functions.dayNight()

# Initialise the CSV file
base_folder = Path(__file__).parent.resolve()
data_file = base_folder/'data.csv'


if __name__ == '__main__':
    print('main.py - AstroPI 2021/2022')

    # Run a loop for three hours
    while (now_time < start_time + timedelta(minutes=2)):
       
        if light == True:
        
            location = ISS.coordinates() # da verificare
        
            capture(name_file, 0)
            
            name_file = datetime.now()
            
            if capture(name_file, 0):
            
                row = (name_file, location.latitude.degrees, location.longitude.degrees, location.elevation.km)
            
                add_csv_data(data_file, row)
        
        # Update the current time
        now_time = datetime.now()
