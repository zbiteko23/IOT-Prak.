from machine import Pin, I2C
from time import sleep_ms

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)
ADDR = 0x27

BL = 0x08
EN = 0x04
RS = 0x01

def write4(data):
    i2c.writeto(ADDR, bytes([data | BL | EN]))
    sleep_ms(1)
    i2c.writeto(ADDR, bytes([data | BL]))
    sleep_ms(1)

def send(value, mode=0):
    high = value & 0xF0
    low = (value << 4) & 0xF0

    write4(high | mode)
    write4(low | mode)

def command(value):
    send(value, 0)

def char(value):
    send(value, RS)

def text(txt):
    for c in txt:
        char(ord(c))

# Inicializace LCD
sleep_ms(50)

write4(0x30)
sleep_ms(5)

write4(0x30)
sleep_ms(5)

write4(0x30)
sleep_ms(5)

write4(0x20)
sleep_ms(5)

command(0x28)  # 4-bit, 2 radky
command(0x0C)  # display ON
command(0x06)  # posun kurzoru
command(0x01)  # vymazat
sleep_ms(5)

# Prvni radek
command(0x80)
text("Raspberry Pi")

# Druhy radek
command(0xC0)
text("I2C funguje!")