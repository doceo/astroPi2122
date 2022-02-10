# moduli utili al daynight
from random import randint
from orbit import ISS
from skyfield.api import load

ephemeris = load('de421.bsp')
timescale = load.timescale()

def dayNight():
    t = timescale.now()
    if ISS.at(t).is_sunlit(ephemeris):
        return True
    else:
        return False

light = dayNight()
print (light)
