from sds011 import SDS011
import mh_z19
from datetime import date,datetime, timedelta
import adafruit_tsl2591
import csv
import os
import time
import board


i2c = board.I2C()
sensor_lux = adafruit_tsl2591.TSL2591(i2c)
sensor_lux.gain = adafruit_tsl2591.GAIN_LOW

pm_sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)

def record_data():
    try:
        co2_values = mh_z19.read(serial_console_untouched=True)
        co2 = co2_values['co2']
    except KeyError:
        print("Co2 failure")
        co2 = -99
        pass
    lux = round(sensor_lux.lux, 2)
    pm_sensor.sleep(sleep=False)
    time.sleep(20)
    pm_values = pm_sensor.query()
    time.sleep(1)
    pm_sensor.sleep()
    pm_2 = pm_values[0]
    pm_10 = pm_values[1]
    if pm_2 is None:
        pm_2 = -99
    if pm_10 is None:
        pm_10 = -99
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows = [now, lux, co2, pm_2, pm_10]
    with open('/home/pi/Desktop/datalogs/datalog_trial_0.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(rows)

i = 0
while True:
    print(f"{i} / inf")
    record_data()
    time.sleep(300)
    i += 1

