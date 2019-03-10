from microbit import *

sleep(10000)
display.scroll(str(button_a.get_presses()))

from microbit import *

while running_time() < 10000:
    display.show(Image.ASLEEP)

display.show(Image.SURPRISED)

from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SURPRISED)
    else:
        display.show(Image.SAD)

display.clear()