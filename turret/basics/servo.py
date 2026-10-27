from machine import Pin, PWM, ADC
import time

servo = PWM(Pin(4), freq=50)

poti = ADC(Pin(1))
poti.atten(ADC.ATTN_11DB)

def winkel():
    inp = poti.read()
    winkel = inp / 4095 * 180
    return winkel

def duty(w):
    ms = 1/90*w + 0.5
    return int(ms/20 * 65535)
try:
    while True:
        print(winkel())
        servo.duty_u16(duty(winkel()))
        time.sleep(0.02)
finally:
    servo.duty_u16(duty(0))  
    time.sleep(1)
    servo.deinit()