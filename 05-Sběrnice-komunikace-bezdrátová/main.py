import bluetooth
from machine import Pin
import time

# =========================
# NASTAVENI LED
# =========================

led = Pin("LED", Pin.OUT)


# =========================
# FUNKCE PRO BLIKANI
# =========================

def blikni(cas):
    led.value(1)
    time.sleep(cas)

    led.value(0)
    time.sleep(0.2)


def blink():
    print("Blikam 10x")

    for i in range(10):
        led.value(1)
        time.sleep(0.5)

        led.value(0)
        time.sleep(0.5)


def fast():
    print("Rychle blikam")

    for i in range(20):
        led.value(1)
        time.sleep(0.1)

        led.value(0)
        time.sleep(0.1)


def sos():
    print("Vysilam SOS")

    # S = ...
    for i in range(3):
        blikni(0.2)

    time.sleep(0.5)

    # O = ---
    for i in range(3):
        blikni(0.7)

    time.sleep(0.5)

    # S = ...
    for i in range(3):
        blikni(0.2)

    led.value(0)


# =========================
# BLUETOOTH
# =========================

ble = bluetooth.BLE()
ble.active(True)

SERVICE_UUID = bluetooth.UUID(
    "12345678-1234-5678-1234-56789abcdef0"
)

CHAR_UUID = bluetooth.UUID(
    "12345678-1234-5678-1234-56789abcdef1"
)

CHAR = (
    CHAR_UUID,
    bluetooth.FLAG_WRITE,
)

SERVICE = (
    SERVICE_UUID,
    (CHAR,),
)

((char_handle,),) = ble.gatts_register_services((SERVICE,))


# =========================
# BLUETOOTH VYSILANI
# =========================

def start_advertising():

    name = "PicoW-Bluetooth"

    name_bytes = name.encode()

    payload = bytearray()

    # BLE flags
    payload += bytes((2, 0x01, 0x06))

    # Nazev zarizeni
    payload += bytes(
        (len(name_bytes) + 1, 0x09)
    ) + name_bytes

    ble.gap_advertise(
        100_000,
        adv_data=payload
    )

    print("Cekam na Bluetooth pripojeni...")


# =========================
# PRIJEM PRIKAZU
# =========================

def bluetooth_event(event, data):

    # Telefon se pripojil
    if event == 1:
        print("Telefon pripojen")

    # Telefon se odpojil
    elif event == 2:
        print("Telefon odpojen")

        start_advertising()

    # Telefon poslal data
    elif event == 3:

        conn_handle, value_handle = data

        if value_handle == char_handle:

            message = ble.gatts_read(
                char_handle
            ).decode().strip().upper()

            print("Prijato:", message)

            # -------------------------
            # PRIKAZY
            # -------------------------

            if message == "ON":

                led.value(1)

                print("LED zapnuta")


            elif message == "OFF":

                led.value(0)

                print("LED vypnuta")


            elif message == "BLINK":

                blink()


            elif message == "FAST":

                fast()


            elif message == "SOS":

                sos()


            elif message == "TEST":

                print("Bluetooth funguje!")


            else:

                print("Neznamy prikaz")


# Zapnuti obsluhy Bluetooth udalosti
ble.irq(bluetooth_event)

# Spusteni vysilani
start_advertising()


# =========================
# HLAVNI PROGRAM
# =========================

while True:
    time.sleep(1)