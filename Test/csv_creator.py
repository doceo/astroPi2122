import csv
from orbit import ISS
from pisense import SenseHat
from datetime import datetime
from pathlib import Path

# Set up Sense Hat
sense = SenseHat()

# Compute the coordinates of the Earth location directly beneath the ISS
location = ISS.coordinates() 

# Define the function that create the CSV and write the firts row
def create_csv(data_file):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time", "Latitude", "Longitude", "Elevation", "Temperature", "Humidity")
        writer.writerow(header)

# Define the function to write the other row with the values
def add_csv_data(data_file, data):
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# Initialise the CSV file
base_folder = Path(__file__).parent.resolve()
data_file = base_folder/'data.csv'
create_csv(data_file)


'''
Questo ciclo può essere un calco tramite il quale si può creare la funzione main

from time import sleep
from datetime import datetime, timedelta

# Record the start and current time
start_time = datetime.now()
now_time = datetime.now()

# Run a loop for three hours
while (now_time < start_time + timedelta(minutes=180)):
    if light == 'Light':
        # funzione capture
        row = (datetime.now(), location.latitude.signed_dma, location.longitude.signed_dms, location.elevation.km, sense.temperature, sense.humidity)
        'row = (datetime.now(), location.latitude.degrees, location.longitude.degrees, location.elevation.km, sense.temperature, sense.humidity)'
        add_csv_data(data_file, row)
        sleep(30)
        # Update the current time
        now_time = datetime.now()
  
  
     
'''
