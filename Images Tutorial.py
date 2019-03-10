from microbit import *
display.show(Image.HAPPY)

from microbit import *
display.show(Image.SAD)

from microbit import *

boat = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "09990")

display.show(boat)

shopping = ["Eggs", "Bacon", "Tomatoes" ]

primes = [2, 3, 5, 7, 11, 13, 17, 19]

mixed_up_list = ["hello!", 1.234, Image.HAPPY]

from microbit import *

display.show(Image.ALL_CLOCKS, loop=False, delay=1000)

from microbit import *

boat1 = Image("05050:"
              "05050:"
              "05050:"
              "99999:"
              "09990")

boat2 = Image("00000:"
              "05050:"
              "05050:"
              "05050:"
              "99999")

boat3 = Image("00000:"
              "00000:"
              "05050:"
              "05050:"
              "05050")

boat4 = Image("00000:"
              "00000:"
              "00000:"
              "05050:"
              "05050:")

boat5 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "05050")

boat6 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]

display.show(all_boats, delay=200)









