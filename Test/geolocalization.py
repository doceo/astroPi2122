from orbit import ISS
from pisense import SenseHat

# Set up Sense Hat
sense = SenseHat()

# Compute the coordinates of the Earth location directly beneath the ISS
location = ISS.coordinates() 

# Latitudine e longtudine espressi in DMS
latitude = location.latitude.signed_dms
longitude = location.longitude.signed_dms
    
# Elevazione
elevation = location.elevation.km
    
# Umidità 
umidity = sense.umidity
    
# Temperature
temperature = sense.temperature
    
    
    
    
