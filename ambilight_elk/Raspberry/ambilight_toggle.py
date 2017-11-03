import RPi.GPIO as gpio
import time
import os

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)

while True:
    input_value = gpio.input(17)
    if input_value == False:
        os.system('if P=$(pgrep hyperion);then service hyperion stop; else service hyperion start; fi')
        time.sleep(0.5)
