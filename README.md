# Raspberry pi pico


## ピン配置

![image](https://user-images.githubusercontent.com/54015319/124367560-2db3e680-dc93-11eb-81b0-5dbb4a602426.png)

## INA219
1. ピン配置

| ina219  | Pico |
-------    | -------  
| SDA      | GP8  |
| SCL      | GP9  |
| VCC      | GP36(3.3V) |
| GND      | GP3(GND) |

## フォトダイオード
1. ピン配置

| PhotoIC | Pico(ADC2) |
-------    | -------  
| カソード     | GP36 |
| アノード     | 1kΩ，GP34 |
| 1kΩ | GND |\

![image](https://user-images.githubusercontent.com/54015319/129685051-cd29f472-2598-422d-b0fa-ba00b70417aa.png
)<br>
カソード(K)に＋電位が加わるようにバイアスして接続し、アノード(A)に負荷抵抗1KΩを接続する。負荷抵抗と並列にコンデンサを入れると高周波成分除去用のローパスフィルタになる。

## SDcard
1. ピン配置

| sd | Pico(SPI1) |
-------    | -------  
| Cds(2)     | GP13  |
| MISO(3)     | GP11 |
| VCC(4)      | GP36(3.3V) |
| SCK(5)     | GP10 |
| GND (6)     | GP3(GND) |
| MOSI(7)      | GP12 |

## 超音波センサ
1. ピン配置

| 超音波センサ| Pico |
-------    | -------  
| trig      | GP12  |
| echo      | GP13  |
| VCC      | GP40(VBUS) |
| GND      | GP3(GND) |

## I2C
### mpu6050

1. ピン配置

| mpu6050  | Pico |
-------    | -------  
| SDA      | GP18  |
| SCL      | GP19  |
| VCC      | GP36(3.3V) |
| GND      | GP3(GND) |


## UART


### GPS
1.ピン配置
| GPS  | Pico |
| ---- | ---- |
| RX   | GP0  |
| TX   | GP1  |
| VCC  | GP36(3.3V) |
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

2. 使い方

親機：MonoStick<br>
子機：Twe-Lite Dip<br>

2.1 設定方法（親機）

＜最初のみ＞

ア）Twe-Lite　Stage APPをダウンロードする<br>
https://mono-wireless.com/jp/products/stage/index.html　

イ）パソコンとMonoStickを繋ぎ、Twe-Lite Stageを立ち上げる<br>
ウ）シリアルポート選択において、MonoStickを選択<br>
エ）アプリ書換でApp_UARTを選択<br>
オ）インタラクティブモードを開く<br>
　1. i を選択し、親機の場合は、121を選択<br>
　2. cを選択し、親機と子機でchannnelを合わせる<br>
　3. mを選択し、UARTモードをDに設定する<br>

2.2 設定方法（子機）

＜最初のみ＞

イ）までは親機と同様<br>
Twe-Lite RにTwe-Lite　Dipをつける<br>
ウ）シリアルポート選択において、Twe-LiteRを選択<br>
エ）アプリ書換でApp_UARTを選択<br>
オ）インタラクティブモードを開く<br>
　1. i を選択し、子機の場合は、120を選択<br>
　2. cを選択し、親機と子機でchannnelを合わせる<br>
　3. mを選択し、UARTモードをDに設定する<br>
　4. bを選択し、GPSの場合は、baudrateを9600にする

＜通常＞

ア）TeraTermを開く<br>
イ）COMを選択<br>
ウ）シリアルポートを115200に設定する<br>
エ）端末の送信をCR＋LFに設定する<br>

3. プログラム

3.1 ピン設定

 ` ` ` 
 uart = UART(1,baudrate=9600,tx=Pin(4),rx=Pin(5))
 ` ` ` 

3.2 書き込み

 ` ` ` 
uart.write(str(gpsTime))
uart.write(str(latitude))
uart.write(str(longitude)) 
 ` ` ` 
 
 数字は送れない
 文字列にする必要がある

## 参考ページ
フォトダイオード<br>
/ http://arms22.blog91.fc2.com/blog-entry-416.html

超音波センサ<br>
/ https://hellobreak.net/raspberry-pi-pico-ultrasonic-distance/

gps<br>
/ https://github.com/ahmadlogs/raspberry-pi-pico-micropython/blob/main/gps-rpi-pico/gps-rpi-pico.py
