from microbit import *

while True:
    reading = accelerometer.get_x()
    if reading > 20:
        display.show("R")
    elif reading < -20:
        display.show("L")
    else:
        display.show("-")

        from microbit import *
import music

while True:
    music.pitch(accelerometer.get_y(), 10)