from machine import I2C
from machine import Pin
from ft6336 import FT6336
import time

i2c = I2C(1, sda=2, scl=3, freq=400000)          # create I2C peripheral at frequency of 400kHz
ts = FT6336(i2c, 4)
               
while True:
    if ts.is_touched():
        points = ts.get_touch_points()
        if len(points) > 0: print(points)
        time.sleep_ms(1)
    else:
        time.sleep_ms(10)
