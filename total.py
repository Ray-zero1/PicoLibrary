import _thread
from machine import Pin, UART, I2C, ADC, Timer, SPI
import utime, time
from mpu6050 import MPU6050
import os
import sdcard

gps_module = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
uart = UART(1,baudrate=115200,tx=Pin(4),rx=Pin(5))
led = Pin(25, Pin.OUT)
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
photoic = ADC(2)
nic_onboard = Pin(17, Pin.OUT)
spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
sd = sdcard.SDCard(spi, Pin(13))
os.mount(sd, '/sd')
os.chdir('sd')
ina = INA219(SHUNT_OHMS, i2c, log_level=INFO)
ina.configure()

t = Timer()
mpu = MPU6050()
buff = bytearray(255)
TIMEOUT = False
FIX_STATUS = False

latitude = ""
longitude = ""
satellites = ""
gpsTime = ""
mode = "rise"
count= 0
def getPositionData(gps_module):
    global FIX_STATUS, TIMEOUT, latitude, longitude, satellites, gpsTime
    timeout = time.time() + 8   # 8 seconds from now
    while True:
        gps_module.readline()
        buff = str(gps_module.readline())
        parts = buff.split(',')
        if (parts[0] == "b'$GPGGA" and len(parts) == 15):
            if(parts[1] and parts[2] and parts[3] and parts[4] and parts[5] and parts[6] and parts[7]):
                latitude = convertToDigree(parts[2])
                # parts[3] contain 'N' or 'S'
                longitude = convertToDigree(parts[4])
                # parts[5] contain 'E' or 'W'
                satellites = parts[7]
                gpsTime = parts[1][0:2] + ":" + parts[1][2:4] + ":" + parts[1][4:6]
                FIX_STATUS = True
                break
                
        if (time.time() > timeout):
            TIMEOUT = True
            break
        utime.sleep_ms(50)
        
#function to convert raw Latitude and Longitude
#to actual Latitude and Longitude
def convertToDigree(RawDegrees):

    RawAsFloat = float(RawDegrees)
    firstdigits = int(RawAsFloat/100) #degrees
    nexttwodigits = RawAsFloat - float(firstdigits*100) #minutes
    
    Converted = float(firstdigits + nexttwodigits/60.0)
    Converted = '{0:.6f}'.format(Converted) # to 6 decimal places
    return str(Converted)

def led_light(self):
    led.value(1)
    utime.sleep(0.1)
    led.value(0)
    utime.sleep(0.1)

def task_gps():
    global TIMEOUT,gpsTime,latitude,longitude
    getPositionData(gps_module)
    uart.write(str(gpsTime)+"\t")
    uart.write(str(latitude)+"\t")
    uart.write(str(longitude)+"\n")     
    if(TIMEOUT == True):
        print("Request Timeout: No GPS data is found.")
        TIMEOUT = False
        uart.write("No data\n")

def solar_culc():
     print("Current: %.3f mA" % ina.current())
     print("Power: %.3f mW" % ina.power())
     uart.write("Current: %.3f mA" % ina.current())
     uart.write("Power: %.3f mW" % ina.power())
     utime.sleep(1)

def read_distance():
    trigger.low()
    utime.sleep_us(10)
    trigger.high()
    utime.sleep(0.00001)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("dinstance: ",distance,"cm")
    
#t.init(period=3000000,mode=t.PERIODIC,callback=task_gps())
while True:
    #t.init(period=1000000,mode=t.PERIODIC,callback=task_gps())
    led_light(led)
    if mode == "rise":
        count += 1
        val = photoic.read_u16() / 1000
        uart.write(str(count)+"\n")
        uart.write("photoic"+str(val)+"\n")
        utime.sleep_ms(2)
        g=mpu.readData()
        uart.write("X:{:.2f}  Y:{:.2f}  Z:{:.2f} \n".format(g.Gx,g.Gy,g.Gz))
        utime.sleep_ms(50)
        with open("/sd/test.txt", "a") as file:
            file.write(str(val) + "\r\n")
        utime.sleep(0.1)
        if val <= 10:
            uart.write("fall")
            with open("/sd/test.txt", "a") as file:
                file.write(str("fall") + "\r\n")
            utime.sleep(0.1)
            mode = "land"
    elif mode == "fall" :
        g=mpu.readData()
        uart.write("X:{:.2f}  Y:{:.2f}  Z:{:.2f} \n".format(g.Gx,g.Gy,g.Gz))
        utime.sleep_ms(50)
        with open("/sd/test.txt", "a") as file:
            file.write("X:{:.2f}  Y:{:.2f}  Z:{:.2f} \n".format(g.Gx,g.Gy,g.Gz)+ "\r\n")
    elif mode == "land" :
        led_light(led)
        nic_onboard.value(1)
        utime.sleep(0.2)
        nic_onboard.value(0)
        uart.write("drive")
        mode = "drive"
    elif mode == "drive":
        solar_calc()
        read_distance()
