import csv
from orbit import ISS
from pisense import SenseHat

# Set up Sense Hat
sense = SenseHat()

# Compute the coordinates of the Earth location directly beneath the ISS
location = ISS.coordinates() 
   

# Open the csv and modify it
with open('data_file', 'w', buffering=1) as f:
    writer = csv.writer(f)
    header = ("Date/time", "Latitude", "Longitude", "Temperature", "Humidity")
    writer.writerow(header)

# Save the data to the file
data = (
  location.latitude.signed_dma,
  location.longitude.signed_dms,
  location.elevation.km
  sense.temperature,
  sense.humidity,
)
add_csv_data(data_file, data)
