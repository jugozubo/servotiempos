# main.py -- put your code here!
from machine import Pin, PWM
from time import sleep
import dht
import network

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

while True:
    sensorTH.measure()
    Temperatura=sensorTH.temperature()
    print("Temperatura: ", Temperatura, "°C")
    if Temperatura>28:
        for i in range(180):
             calculoangulo(i)
             sleep(0.01)
    
