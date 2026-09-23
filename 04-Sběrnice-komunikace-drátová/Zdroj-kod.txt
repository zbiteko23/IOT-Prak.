from machine import Pin, SPI
from time import sleep

# SPI
spi = SPI(
    0,
    baudrate=1000000,
    polarity=0,
    phase=0,
    sck=Pin(18),
    mosi=Pin(19)
)

cs = Pin(17, Pin.OUT)
cs.value(1)

def poslat(registr, hodnota):
    cs.value(0)
    spi.write(bytes([registr, hodnota]))
    cs.value(1)

# Nastavení MAX7219
poslat(0x0F, 0)     # test displeje vypnutý
poslat(0x0C, 1)     # zapnutí displeje
poslat(0x0B, 7)     # všech 8 řádků
poslat(0x09, 0)     # bez dekódování
poslat(0x0A, 3)     # jas 0-15

# Smazání displeje
for i in range(1, 9):
    poslat(i, 0)

# Smajlík :)
smajlik = [
    0b00111100,
    0b01000010,
    0b10100101,
    0b10000001,
    0b10100101,
    0b10011001,
    0b01000010,
    0b00111100
]

for radek in range(8):
    poslat(radek + 1, smajlik[radek])