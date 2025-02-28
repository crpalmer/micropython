from machine import I2C
from machine import Pin

class FT6336:
    def __init__(self, i2c, int_gpio):
        self.i2c = i2c
        self.int = Pin(int_gpio, mode=Pin.IN)
        self.addr = 0x38
        self.G_MODE_REG = 0xa4
        self.TD_STATUS_REG = 0x02
        self.P1_X_REG = 0x03
        self.P1_Y_REG = 0x05
        self.P2_X_REG = 0x09
        self.P2_Y_REG = 0x0b

        self.i2c.writeto_mem(self.addr, self.G_MODE_REG, b'\x00')     # Set polling mode, it will signal touch constantly while touched (using INT pin)

    def is_touched(self):
        #print(self.int.value())
        return self.int.value() == 0

    def get_touch_points(self):
        touch_points = []
        n_touches = self.i2c.readfrom_mem(self.addr, self.TD_STATUS_REG, 1)[0]
        if n_touches >= 1:
            touch_points.append(self.read_touch_point(self.P1_X_REG))
            touch_points.append(self.read_touch_point(self.P1_Y_REG))
            if n_touches >= 2:
                touch_points.append(self.read_touch_point(self.P2_X_REG))
                touch_points.append(self.read_touch_point(self.P2_Y_REG))
        return touch_points

    def read_touch_point(self, reg):
        bytes = self.i2c.readfrom_mem(self.addr, reg, 2)
        return int(bytes[1]) | ((int(bytes[0]) & 0x07) << 8)
