import asyncio
from smartplug import SmartPlug
import time
import board
import neopixel
from rpi_ws281x import Color
import board
import neopixel
import time
import os
from digitalio import DigitalInOut, Direction, Pull
from multiprocessing import Process
import sys
import serial
import time
from gpiozero import LED
from time import sleep
from PyP100 import PyP100
p100 = PyP100.P100("192.168.43.55", "CENSORED", "CENSORED")
p100.handshake()
p100.login()

led = LED(17)

pixel_pin = board.D18

num_pixels = 144

ORDER = neopixel.RGB
pixels= neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

async def turnOffHeater():

    p = SmartPlug("CENSORED")

    await p.update()

    await p.turn_off()

async def turnOnHeater():
    p = SmartPlug("CENSORED")

    await p.update()

    await p.turn_on()
    
async def turnOffFan():

    p100.turnOff()

async def turnOnFan():
    
    p100.turnOn()

print('START')


rocket = 0

def func1():
    global rocket
    print ('start func1')
    import serial
    try:
        print('i tried1')
        ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
        time.sleep(2)
        ser.write(b'start')
    except:
        print('errrrrrooorrrrr1')
    try:
        print('i tried2')
        ser1 = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        time.sleep(2)
        ser1.write(b'start')
    except:
        print('errrrrrooorrrrr2')
    try:
        print('i tried2')
        ser1 = serial.Serial('/dev/ttyACM2', 9600, timeout=1)
        time.sleep(2)
        ser1.write(b'start')
    except:
        print('errrrrrooorrrrr2')
        
    

def func2():
    global rocket
    start = time.time()
    os.system("sudo -u pi bash -c 'cvlc movie.mov'")

def func3():
    global rocket
    
    

while True:
    import urllib.request
    import json
    with urllib.request.urlopen('https://climatator-web.vercel.app/api/status') as response:
       res = json.loads(response.read().decode("utf-8"))
       print(res)
       if res['video'] == 1:
            print('hi!')
            import serial
            try:
                print('i tried1')
                ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
                time.sleep(2)
                ser.write(b'start')
            except:
                print('errrrrrooorrrrr1')
            try:
                print('i tried2')
                ser1 = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
                time.sleep(2)
                ser1.write(b'start')
            except:
                print('errrrrrooorrrrr2')
            time.sleep(13)
            try:
                asyncio.run(turnOnHeater())
            except:
                print('Heated Did Not Activate')
            time.sleep(10)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            sleep(6)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            sleep(23)
            try:
                asyncio.run(turnOffHeater())
            except:
                print('Could not turn off heater')
            try:
                asyncio.run(turnOnFan())
            except:
                print('Could not turn on fan')
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
            sleep(28)
            try:
                asyncio.run(turnOffFan())
            except:
                print('Could not turn off fan')
            
            urllib.request.urlopen('https://climatator-web.vercel.app/api/finished')
