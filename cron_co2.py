#!/usr/bin/python3

import board
import adafruit_scd30
import time
from datetime import date,datetime


scd = adafruit_scd30.SCD30(board.I2C())

while True:
    if scd.data_available == 0:
        time.sleep(1)
        continue
    print("Data available?", scd.data_available)
    print("CO2:", scd.CO2, "PPM")
    print("Temperature:", scd.temperature, "degrees C")
    print("Humidity:", scd.relative_humidity, "%%rH")
    file_name = "/home/pi/proj/CO2_sensor/" + str(date.today()) + ".log"
    f = open(file_name, "a")
    f.write(str(datetime.now()) + "," + str(scd.CO2) + "," + str(scd.temperature) + "," + str(scd.relative_humidity) + "\n")
    f.close()
    break

