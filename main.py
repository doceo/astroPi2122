# Personal Modules
from functions import *

# Module for path
from pathlib import Path

# Module for warm-up
from time import sleep


# Main code
if __name__ == '__main__':
    print('main.py - AstroPI 2021/2022')

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
        light = dayNight()
        print(light)

        # If the ISS is orbiting above the illuminated part of the earth run this code
        if light == True:
            
            # Determine the path and name of the images
            image_name = str(datetime.now().strftime("%Y%m%d-%H%M%S"))
            path_image = str(base_folder) + '/images/' + image_name             
            print(image_name)
            
            # Capturing the images
            if capture(path_image, 1, data_file):
                print("save")
        
        # Update the current time
        now_time = datetime.now()
        print(now_time)
        
        # Raspberry warm-up time in order to avoid thermal-throttling
        sleep(8)