# main.py -- put your code here!
from machine import Pin, PWM, SPI
from time import sleep
import dht
import network
import time
import ntptime
import max7219

spi=SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23)) #mosi=DIN
cs=Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, cs, 4)

display.brightness(15)
display.fill(0)
display.text("Hola", 0, 0, 1)
display.show()

MiWIFI = network.WLAN(network.STA_IF)
MiWIFI.active(True)

MiWIFI.connect("WIFI-ITM","")

while not MiWIFI.isconnected():
    print("Me estoy conectando, espereme un momentico...")
    sleep(1)

print("Conectado OK, mandeme lo que sea")





sensorTH=dht.DHT11(Pin(12))
servo = PWM(Pin(14), freq=50)

def calculoangulo(angle):
    valor=int((angle/180*102)+25)
    servo.duty(valor)

try:
    ntptime.settime()
except:
    raise Exception("npttime.settime() failed. No network connection.")

def getNow():
    local_time = -18000
    return time.gmtime(time.time() + local_time)

while True:
    x=getNow()
    print(x)
    sleep(1)
    try:
        sensorTH.measure()
        Temperatura=sensorTH.temperature()
        print("Temperatura: ", Temperatura, "°C")
        if Temperatura>28:
            for i in range(180):
                calculoangulo(i)
                sleep(0.01)
    except OSError as e:
        print("Error al leer el sensor: ", e)    
