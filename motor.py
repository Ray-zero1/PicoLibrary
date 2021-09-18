from machine import Pin, PWM
from time import sleep
import utime

#frequency = 50

#BIN2 = 21
#BIN1 = 20
#STBY = 16
#AIN1 = 10
#AIN2 = 11
#PWMA = 26 
#PWMB = 27
#ofsetA = 1
#ofsetB = 1


BIN1 = Pin(20, Pin.OUT)
BIN2 = Pin(21, Pin.OUT)
STBY = Pin(16, Pin.OUT)
PWMB = Pin(27, Pin.OUT)
AIN1 = Pin(6, Pin.OUT)
AIN2 = Pin(7, Pin.OUT)
PWMA = Pin(26, Pin.OUT)

def front():
    # 正転
    BIN1.value(1)
    BIN2.value(0)
    AIN1.value(1)
    AIN2.value(0)
    PWMB.value(1)
    STBY.value(1)
    PWMA.value(1)
    utime.sleep_ms(100)
    
def back():
    # 逆転
    BIN1.value(0)
    BIN2.value(1)
    AIN1.value(0)
    AIN2.value(1)
    PWMB.value(1)
    STBY.value(1)
    PWMA.value(1)
    utime.sleep_ms(100)
    
def turn_right():
    BIN1.value(1)
    BIN2.value(0)
    AIN1.value(0)
    AIN2.value(0)
    PWMB.value(1)
    STBY.value(1)
    PWMA.value(1)
    utime.sleep_ms(100)
    
def turn_left():
    BIN1.value(0)
    BIN2.value(0)
    AIN1.value(1)
    AIN2.value(0)
    PWMB.value(1)
    STBY.value(1)
    PWMA.value(1)
    utime.sleep_ms(100)
    
def stop(self):
    #停止
    BIN1.value(0)
    BIN2.value(0)
    AIN1.value(0)
    AIN2.value(0)
    PWMB.value(1)
    STBY.value(1)
    PWMA.value(1)
    utime.sleep_ms(100)

count = 0
while True:
    front()
