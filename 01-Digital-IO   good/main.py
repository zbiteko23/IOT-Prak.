from machine import Pin
from time import sleep

# LED = digitální výstup
led = Pin(15, Pin.OUT)

# Tlačítko = digitální vstup
button = Pin(14, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        led.value(1)       # LED zapnout
    else:
        led.value(0)       # LED vypnout

    sleep(0.01)