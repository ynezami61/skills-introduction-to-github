from machine import Pin 
from time import sleep 
led_pin=2
led=Pin(led_pin,Pin.OUT)
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
