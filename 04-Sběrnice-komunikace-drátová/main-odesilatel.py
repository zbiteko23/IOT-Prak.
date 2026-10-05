from machine import UART, Pin
from time import sleep

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
    uart.write("Ahoj z Pico 1!\n")
    print("Odeslano")
    sleep(2)