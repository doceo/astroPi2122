# MODULI PERSONALI
from functions import *

# MODULI PER CSV
import csv

from pathlib import Path
from time import sleep

'''
descrizioni variabili globali
'''

if __name__ == '__main__':
    print('main.py - AstroPI 2021/2022')

    # Initialise the CSV file
    base_folder = Path(__file__).parent.resolve()
    data_file = base_folder/'data.csv'

    create_csv(data_file)

    start_time = datetime.now()
    now_time = datetime.now()


    # Run a loop for three hours
    while (now_time < start_time + timedelta(minutes=3)):
        
        # Variables for the dayNight function
     
        #light = dayNight()
        light = True
        print(light)

        if light == True:
            
            image_name = str(datetime.now().strftime("%Y%m%d-%H%M%S"))
            path_image = str(base_folder) + "/" + image_name             
            
            print(image_name)

            # Compute the coordinates of the Earth location directly beneath the ISS
            location = ISS.coordinates()
            print(location)

            if capture(image_name, 1, data_file):
                print("save")
                row = (image_name, location.latitude.degrees, location.longitude.degrees, location.elevation.km)
                print(row)
                add_csv_data(data_file, row)
        
        # Update the current time
        now_time = datetime.now()
        print(now_time)
        sleep(23) # si deve scattare una foo ogni 23 secondi per avere circa 500 fotografie