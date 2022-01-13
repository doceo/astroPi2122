import csv
from phatlib import Path

base_folder = Path(__file__).parent.resolve()

# Initialise the CSV file
data_file = base_folder/'data.csv'
create_csv_file(data_file)

# Open the csv and modify it
with open(data_file, 'w', buffering=1) as f:
    writer = csv.writer(f)
    header = ("Date/time", "Latitude", "Longitude", "Temperature", "Humidity")
    writer.writerow(header)
  
''' ciclo dove quando scatti una foto scrivere una riga del csv
# Save the data to the file
data = (
  datatime.now(),
  latitude,
  longitude,
  temperature,
  humidity,
)
add_csv_data(data_file, data)'''
