from machine import Pin, PWM, I2C, UART, SPI, ADC
from time import sleep
import utime
import hc_sr04


led = Pin(25, Pin.OUT)
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)




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
    
def stop():
    #停止
    BIN1.value(0)
    BIN2.value(0)
    AIN1.value(0)
    AIN2.value(0)
    PWMB.value(1)
    STBY.value(1)
    PWMA.value(1)
    utime.sleep_ms(100)

def read_distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep(0.00001)
    trigger.low()
    while echo.value() == False:
        signaloff = utime.ticks_us()
    while echo.value() == True:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

count = 0
while True:
    
    try:
        if count < 3 :
            distance = read_distance()
            distance = round(distance,2)
            print(distance)
            front()
            utime.sleep(0.1)
            if distance <= 50:
                count+=1
                if count == 3:
                    stop()
                    utime.sleep(1)
                    turn_right()
                    utime.sleep(0.5)
                    stop()
                    utime.sleep(1)
                    front()
                    utime.sleep(2)
                    stop()
                    utime.sleep(1)
                    turn_left()
                    utime.sleep(0.5) 
                    count = 0
    except NameError:
        continue
        
