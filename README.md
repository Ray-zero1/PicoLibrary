# Raspberry pi pico


## ピン配置

![image](https://user-images.githubusercontent.com/54015319/124367560-2db3e680-dc93-11eb-81b0-5dbb4a602426.png)

## UART


### GPS
1.ピン配置
| GPS  | Pico |
| ---- | ---- |
| RX   | GP0  |
| TX   | GP1  |
| VCC  | GP40(VBUS) |
| GND  | GP3(GND) |

2. プログラム

ピンを設定

 ` ` ` 
gps_module = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
 ` ` ` 

後は、gps.pyを参考

### Twe-Lite
1. ピン配置

| Twe-Lite  | Pico       |
----      | ----       
| GP7(RX)   | GP4        |
| GP6(TX)   | GP5        |
| GP17(BTS) | GP3(GND)   |
| VCC       | GP36(3.3V) |
| GND       | GP3(GND)   |

2. プログラム

2.1 ピン設定
 ` ` ` 
 uart = UART(1,baudrate=9600,tx=Pin(4),rx=Pin(5))
 ` ` ` 

2.2 書き込み
 ` ` ` 
uart.write(str(gpsTime))
uart.write(str(latitude))
uart.write(str(longitude)) 
 ` ` ` 
 数字は遅れない
 文字列にする必要がある
