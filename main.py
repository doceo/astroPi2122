# MODULI PERSONALI
import functions

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

location = ISS.coordinates() 

# Initialise the CSV file
base_folder = Path(__file__).parent.resolve()
data_file = base_folder/'data.csv'


def capture(name):
    
    base_folder = Path(__file__).parent.resolve()
    name_image = str(base_folder) + "/images/" + str(name) +".jpg"
    camera = PiCamera()
    camera.resolution = (1296,972)
    # Camera warm-up time
    sleep(2)
    camera.capture(f"{name_image}")
    return True  # va verificata la scrittura



# Define the function that create the CSV and write the firts row
def create_csv(data_file):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time", "Latitude", "Longitude", "Elevation", "Temperature", "Humidity")
        writer.writerow(header)
create_csv(data_file)

# Define the function to write the other row with the values
def add_csv_data(data_file, data):
    with open(data_file, 'a') as f:

        row = (data, location.latitude.signed_dma, location.longitude.signed_dms, location.elevation.km)
        writer = csv.writer(f)
        writer.writerow(data)


if __name__ == '__main__':
    print('main.py - AstroPI 2021/2022')

    # Run a loop for three hours
    while (now_time < start_time + timedelta(minutes=2)):
        
        
        # CAPTURE AND SAVE
        name_file = datetime.now()
        if capture(name_file):
            add_csv_data(data_file, name_file)
        
    
        # Update the current time
        now_time = datetime.now()
