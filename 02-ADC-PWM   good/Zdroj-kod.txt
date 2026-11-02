from machine import Pin, ADC, PWM
from time import sleep

# Potenciometr na ADC0 (GP26)
pot = ADC(26)

# LED ovládaná pomocí PWM
led = PWM(Pin(15))

# Frekvence PWM
led.freq(1000)

while True:
    # Přečtení potenciometru
    hodnota = pot.read_u16()

    # Nastavení jasu LED
    led.duty_u16(hodnota)

    # Výpis hodnoty do Thonny
    print("ADC:", hodnota)

    sleep(0.1)