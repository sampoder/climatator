import asyncio
from smartplug import SmartPlug
import time
import board
import neopixel
from rpi_ws281x import *

pixel_pin = board.D18

num_pixels = 144

ORDER = neopixel.RGB
pixels= neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)
 

async def turnOffFan():
    p = SmartPlug("192.168.1.144")

    await p.update()

    await p.turn_off()

async def turnOnFan():
    p = SmartPlug("192.168.1.144")

    await p.update()

    await p.turn_on()

def colorWipe(strip, color, color2, color3, wait_ms=50):
    for i in range(num_pixels):
	    strip.fill(color)
    while True:
        for i in range(num_pixels):
            strip[i] = color2
            strip.show()
            time.sleep(wait_ms/10000.0)
        for i in range(num_pixels):
            strip[i] = color3
            strip.show()
            time.sleep(wait_ms/10000.0)
        for i in range(num_pixels):
            strip[i] = color
            strip.show()
            time.sleep(wait_ms/10000.0)
    strip.clear()
    
colorWipe(pixels, Color(40, 0, 0),  Color(40, 5, 0),  Color(40, 10, 0))
