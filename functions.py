from random import randint
from orbit import ISS
from skyfield.api import load


def funcTest():
    return "facciamo un test con numero random: " + str(randint(1, 100))


ephemeris = load('de421.bsp')
timescale = load.timescale()


def dayNight():
    t = timescale.now()
    if ISS.at(t).is_sunlit(ephemeris):
        return True
    else:
        return False


if __name__ == '__main__':
    print(funcTest())
