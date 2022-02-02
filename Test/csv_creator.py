import csv
from orbit import ISS

from pathlib import Path
from time import sleep
from datetime import datetime, timedelta

# Initialise the CSV file
base_folder = Path(__file__).parent.resolve()
data_file = base_folder/'data.csv'


# Compute the coordinates of the Earth location directly beneath the ISS
location = ISS.coordinates() 
print(location)

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

    create_csv(data_file)

    # Record the start and current time
    start_time = datetime.now()
    now_time = datetime.now()

    # funzione capture
    row = (datetime.now(), location.latitude.signed_dma, location.longitude.signed_dms, location.elevation.km)
    add_csv_data(data_file, row)
