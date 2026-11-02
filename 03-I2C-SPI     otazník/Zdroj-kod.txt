from machine import Pin, I2C, ADC
from pico_i2c_lcd import I2cLcd
from time import sleep

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)
lcd = I2cLcd(i2c, 39, 2, 16)
pot = ADC(Pin(26))

lcd.putstr("Potenciometr:")

while True:
    hodnota = pot.read_u16()
    lcd.move_to(0, 1)
    lcd.putstr(str(hodnota) + "     ")
    sleep(0.2)