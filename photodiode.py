import machine
import utime

adc = machine.ADC(0)

while True:
    val = adc.read_u16() / 1000
    print(val)
    utime.sleep(2)
