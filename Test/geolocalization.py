from orbit import ISS
from sense_hat import SenseHat

# Set up Sense Hat
sense = SenseHat()

# Compute the coordinates of the Earth location directly beneath the ISS
    location = ISS.coordinates() 

# Latitudine e longtudine espressi in DMS
Latitudine = location.latitude.signed_dms
Longitudine = location.longitude.signed_dms
    
# Latitudine e longtudine espressi in DD
Latitudine = location.latitude.degrees:.1f
Longitudine = location.longitude.degrees:.1f

# Elevazione
Elevation = location.elevation.km
    
# Umidità 
umidity = sense.umidity
    
# Temperature
temperature = sense.temperature
    
    
    
    
