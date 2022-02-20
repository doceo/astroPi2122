# Personal Modules
from utils import *

# Module for path of the CSV file
from pathlib import Path

# Module for warm-up
from time import sleep

# Module for the while loop
from datetime import datetime, timedelta

# Main code
def main_function():
    # Initialise the CSV file
    base_folder = Path(__file__).parent.resolve()
    data_file = str(base_folder) + '/data.csv'
    create_csv(data_file)

    # Collecting current time
    start_time = datetime.now()
    now_time = datetime.now()

    # Run loop for three hours
    while (now_time < start_time + timedelta(minutes=180)):
        
        # Variables for the dayNight function
        timescale = load.timescale().now()
        
        # Load ephemeris (high accuracy table with position of celestial objects)
        ephemeris = load('de421.bsp')
        light = dayNight()
        print(light)

        # If the ISS is orbiting above the illuminated part of the earth run this code
        if light == True:
            
            # Determine the path and name of the images
            # Image's name is: YYMMDD-HHMMSS
            image_name = str(datetime.now().strftime("%Y%m%d-%H%M%S"))
            path_image = str(base_folder) + '/images/' + image_name             
            print(image_name)
            
            # Capturing the images
            if capture(path_image, data_file, 1):
                print("save")
        
        # Update the current time
        now_time = datetime.now()
        print(now_time)
        
        # Raspberry warm-up time in order to avoid thermal-throttling
        sleep(11.5)

if __name__ == '__main__':
    print('main.py - AstroPI 2021/2022')
    main_function()