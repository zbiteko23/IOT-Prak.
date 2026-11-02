import bluetooth
from machine import Pin
import time

# Vestavena LED na Pico W
led = Pin("LED", Pin.OUT)

# Zapnuti Bluetooth
ble = bluetooth.BLE()
ble.active(True)

# UUID sluzby a charakteristiky
SERVICE_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef0")
CHAR_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef1")

# Charakteristika umozni zapis z telefonu
CHAR = (
    CHAR_UUID,
    bluetooth.FLAG_WRITE,
)

SERVICE = (
    SERVICE_UUID,
    (CHAR,),
)

# Registrace sluzby
((char_handle,),) = ble.gatts_register_services((SERVICE,))

# Co se stane pri Bluetooth udalosti
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
            message = ble.gatts_read(char_handle).decode().strip().upper()

            print("Prijato:", message)

            if message == "ON":
                led.value(1)
                print("LED zapnuta")

            elif message == "OFF":
                led.value(0)
                print("LED vypnuta")


ble.irq(bluetooth_event)


# Spusteni Bluetooth vysilani
def start_advertising():

    name = "PicoW-Bluetooth"
    name_bytes = name.encode()

    payload = bytearray()

    # BLE flags
    payload += bytes((2, 0x01, 0x06))

    # Nazev zarizeni
    payload += bytes((len(name_bytes) + 1, 0x09)) + name_bytes

    ble.gap_advertise(100_000, adv_data=payload)

    print("Cekam na Bluetooth pripojeni...")


start_advertising()

while True:
    time.sleep(1)