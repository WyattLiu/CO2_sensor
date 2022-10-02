#!/usr/bin/python3

import board
import adafruit_scd30
import time

scd = adafruit_scd30.SCD30(board.I2C())

while True:
    if scd.data_available == 0:
        time.sleep(1)
        continue
    print("Data available?", scd.data_available)
    print("CO2:", scd.CO2, "PPM")
    print("Temperature:", scd.temperature, "degrees C")
    print("Humidity:", scd.relative_humidity, "%%rH")
    time.sleep(1)
