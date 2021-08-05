import deneyap
from time import sleep
from machine import Pin ,PWM
servo = PWM(Pin(deneyap.PWM0),freq =50)
while True:
    servo.duty(110)
    sleep(0.1)         
    servo.duty(40)
    sleep(0.1)