from machine import Pin, UART

uart = UART(0, 9600, rx=Pin(1))
led = Pin(16, Pin.OUT)

while True:
    if uart.any():
        data = uart.read()
        if data:
            led.value(data[-1:] == b"1")