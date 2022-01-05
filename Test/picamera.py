from picamera import *
import time

#creazione della variabile camera
camera = PiCamera()

#inizio registrazione
camera.start_preview()

#ciclo di while che stabilisce l'intervallo in secondi tra gli scatti
while(1):
    for i in range(9):
        time.sleep(1800)

#	data = '{:>6.0f}'.format(time.monotonic())

#cattura immagine
camera.capture('image/image%s.jpg' % i)

#termine registrazione
camera.stop_preview()