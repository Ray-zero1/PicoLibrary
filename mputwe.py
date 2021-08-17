from machine import Pin, UART, I2C
import utime, time
from mpu6050 import MPU6050

uart = UART(1,baudrate=115200,tx=Pin(4),rx=Pin(5))
led = Pin(25, Pin.OUT)
mpu = MPU6050()

def led_light(self):
    led.value(1)
    utime.sleep(0.1)
    led.value(0)
    utime.sleep(0.1)
    
while True:
    led_light(led)
    g=mpu.readData()
    print("X:{:.2f}  Y:{:.2f}  Z:{:.2f}".format(g.Gx,g.Gy,g.Gz))
    uart.write("X:{:.2f}  Y:{:.2f}  Z:{:.2f} \n".format(g.Gx,g.Gy,g.Gz))
    utime.sleep_ms(100)
