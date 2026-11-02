from machine import Pin, UART
from time import sleep

uart = UART(0, 9600, tx=Pin(0))
tl = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    uart.write("1" if tl.value() == 0 else "0")
    sleep(0.1)