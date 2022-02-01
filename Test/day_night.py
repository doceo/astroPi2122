"""TA satellite is generally only visible to a ground observer when there is still sunlight up at its altitude. The
satellite will visually disappear when it enters the Earth’s shadow and reappear when it comes out of eclipse. If you
are planning to observe a satellite visually, rather than with radar or radio, you will want to know which satellite
passes are in sunlight. Knowing a satellite’s sunlit periods is also helpful when modeling satellite power and
thermal cycles as it goes in and out of eclipse.

Skyfield provides a simple geometric estimate for this through the is_sunlit() method. Given an ephemeris with which
it can compute the Sun’s position, it will return True when the satellite is in sunlight and False otherwise. """

from time import sleep
from orbit import ISS  # sei sicuro serva?
from skyfield.api import load



ephemeris = load('de421.bsp')
timescale = load.timescale()

'''
questo script deve diventare una funzione da richiamare, non un ciclo.
definisci una funzione dayNight() che restituisce true o false quando richiamata.
testiamola nel main che ho inserito sotto

'''

while True:
    t = timescale.now()
    if ISS.at(t).is_sunlit(ephemeris):
        sunlight = True
    else:
        sunlight = False
    sleep(30)


if __name__ == '__main__':
    pass