from microbit import *
import random

names = ["Mary", "Yolanda", "Damien", "Alia", "Kushal", "Mei Xiu", "Zoltan" ]

display.scroll(random.choice(names))

from microbit import *
import random

display.show(str(random.randint(1, 6)))

from microbit import *
import random

answer = random.randrange(100) + random.random()
display.scroll(str(answer))

from microbit import *
import random

random.seed(1337)
while True:
    if button_a.was_pressed():
        display.show(str(random.randint(1, 6)))