from machine import Pin, SPI
from ili9341 import Display, color565
from xglcd_font import XglcdFont

spi = SPI(1, sck=Pin(10), mosi=Pin(11))
display = Display(spi, dc=Pin(8), cs=Pin(9), rst=Pin(7), width=320, height=240, rotation=90)
font = XglcdFont('fonts/Unispace12x24.c', 12, 24)

display.fill_rectangle(10, 10, 50, 50, color565(255, 0, 0))
display.fill_rectangle(50, 50, 10, 10, color565(0, 2550, 0))
display.draw_text(10, 70, 'Hello world', font, color565(0, 0, 255))
