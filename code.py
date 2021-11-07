"""RGB Flashing Lights

When button A is pressed, a red light is shown on all neopixels.
When button B is pressed, a green light is shown on all neopixels.
"""

import time
from adafruit_circuitplayground.express import cpx
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Here we define three different colors using a tuple structure.  There
# are three numbers in the tuple, each representing how much of a
# specific color should be displayed.  For the CPE board, the three
# colors are Red, Green, and Blue (RGB).  The values possible ranges
# from 0 (none of that color) to 256 (all of that color).  In this
# example we only do three colors; Red, Green, and Blue.
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# NeoPixels on a Circuit Playground Express are numbered 0 to 9 
# counter-clockwise starting from the pixel at the top and left
# of the centerline.

# the leftmost pixel by button A
cpx.pixels[2] = RED
# the rightmost pixel by button B
cpx.pixels[7] = GREEN

# the keyboard object!
# sleep for a bit to avoid a race condition on some systems
# (a race condition is when two things happen at the same time, and they
# cause a problem with each other)
time.sleep(1)
kbd = Keyboard(usb_hid.devices)
# we're americans :)
layout = KeyboardLayoutUS(kbd)

# The mute button on the keyboard uses Keycode
MUTE = 0xef

# debounce delay (in seconds)
# this prevents us from accidentally sending lots of keypresses
# if the button is pressed lightly
DEBOUNCE_DELAY = 0.5

# This is the main loop of the board.  This will run infinetly.
while True:

    # When button A is detected having been pressed, 
    # make all pixels RED
    if cpx.button_a:
        # make the lights RED
        cpx.pixels.fill(RED)

        # loop doing nothing until the button is released
        while cpx.button_a:
            pass

        # send a MUTE key shortcut for MS Teams
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)
        
        # introduce a brief delay to prevent repeats
        time.sleep(DEBOUNCE_DELAY)
    
    # When button B is detected having been pressed, 
    # make all pixels GREEN
    elif cpx.button_b:
        # make the lights GREEN
        cpx.pixels.fill(GREEN)

        # loop doing nothing until the button is released
        while cpx.button_b:
            pass

        # send a MUTE key shortcut for MS Teams
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)
        
        # introduce a brief delay to prevent repeats
        time.sleep(DEBOUNCE_DELAY)

