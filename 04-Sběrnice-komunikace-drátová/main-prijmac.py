from machine import UART, Pin
from time import sleep

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
    if uart.any():
        zprava = uart.readline()

        if zprava:
            print("Prijato:", zprava.decode().strip())

    sleep(0.1)