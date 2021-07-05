from machine import Pin,SPI
import os
import sdcard
import utime

trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
sd = sdcard.SDCard(spi, Pin(13))
os.mount(sd, '/sd')
os.chdir('sd')
    
def read_distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep(0.00001)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

 
while True:
        distance = read_distance()
        print("dinstance: ",distance,"cm")
        # SD Card output
        file = open('/sd/test.txt', 'w')
        file.write(str(distance) + "\r\n")
        file.close()
        utime.sleep(0.1)
