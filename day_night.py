"""TA satellite is generally only visible to a ground observer when there is still sunlight up at its altitude. The
satellite will visually disappear when it enters the Earth’s shadow and reappear when it comes out of eclipse. If you
are planning to observe a satellite visually, rather than with radar or radio, you will want to know which satellite
passes are in sunlight. Knowing a satellite’s sunlit periods is also helpful when modeling satellite power and
thermal cycles as it goes in and out of eclipse.

Skyfield provides a simple geometric estimate for this through the is_sunlit() method. Given an ephemeris with which
it can compute the Sun’s position, it will return True when the satellite is in sunlight and False otherwise. """

from orbit import ISS
from skyfield.api import load

# load ephemeris (high accuracy table with position of celestial objects)
ephemeris = load('de421.bsp')
timescale = load.timescale()


# this function returns true if the satellite is in sunlight and returns false if the satellite is not in sunlight
def dayNight():
    t = timescale.now()
    if ISS.at(t).is_sunlit(ephemeris):
        return True
    else:
        return False


if __name__ == '__main__':
    
    print(dayNight())
