from orbit import ISS

def geographical_values():
    # Compute the coordinates of the Earth location directly beneath the ISS
    location = ISS.coordinates() 

    # Valori espressi in DMS
    print(f'Lat: {location.latitude.signed_dms()}, Long: {location.longitude.signed_dms()}') 
    
    # Valori espressi in DD
    print(f'Lat: {location.latitude.degrees:.1f}, Long: {location.longitude.degrees:.1f}')

    # Unico modo per esprimere elevazione
    print(f'Elevation: {location.elevation.km}')