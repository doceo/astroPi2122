import csv
'import geolocalization'



# Open the csv and modify it
with open('data_file', 'w', buffering=1) as f:
    writer = csv.writer(f)
    header = ("Date/time", "Latitude", "Longitude", "Temperature", "Humidity")
    writer.writerow(header)

'''
# Save the data to the file
data = (
  datatime.now(),
  latitude,
  longitude,
  temperature,
  humidity,
)
add_csv_data(data_file, data)
'''