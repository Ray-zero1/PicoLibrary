from machine import Pin, I2C
from ina219 import INA219
from logging import INFO
import utime
SHUNT_OHMS = 0.1

i2c = I2C(0,scl=Pin(9),sda=Pin(8))
ina = INA219(SHUNT_OHMS, i2c, log_level=INFO)
ina.configure()

while True:
    print("Bus Voltage: %.3f V" % ina.voltage())
    print("Bus Voltage: %.3f V" % ina.supply_voltage())
    print("Current: %.3f mA" % ina.current())
    print("Power: %.3f mW" % ina.power())
    utime.sleep(1)
    
