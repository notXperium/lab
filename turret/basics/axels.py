from machine import Pin, PWM, ADC
import time

pan = PWM(Pin(21), freq=50)
tilt = PWM(Pin(15 ), freq=50)

VRx = ADC(Pin(5))
VRy = ADC(Pin(6))
SW = Pin(7, Pin.IN, Pin.PULL_UP)

VRx.atten(ADC.ATTN_11DB)
VRy.atten(ADC.ATTN_11DB)

def winkel_X(inp):
    if inp < 2414:
        winkel = (inp-50) / (2414-50) * 90
    else:
        winkel = (inp-2414) / (4095-2414) * 90 + 90
    if winkel < 0: winkel = 0
    if winkel > 180: winkel = 180
    return winkel

def winkel_Y(inp):
    if inp < 2003:
        winkel = inp / 2003 * 90
    else:
        winkel = (inp-2003) / (4095-2003) * 90 + 90
    if winkel < 0: winkel = 0
    if winkel > 180: winkel = 180
    return winkel

def duty(w):
    ms = 1/90*w + 0.5
    return int(ms/20 * 65535)

Null_X = duty(0)
Null_Y = duty(0)

pan.duty_u16(Null_X)
tilt.duty_u16(Null_Y)
time.sleep(1)

oldX = 0
oldY = 0
try:
    while True:
        if SW.value() == 0:
            pan.duty_u16(Null_X)
            tilt.duty_u16(Null_Y)
            oldX = 0
            oldY = 0
        else:
            x = winkel_X(VRx.read())
            y = winkel_Y(VRy.read())
            if abs(x- oldX) > 1.0: 
                pan.duty_u16(duty(x))
                oldX = x
            if abs(y - oldY) > 1.0:
                tilt.duty_u16(duty(y))
                oldY = y
        time.sleep(0.02)
finally:
    pan.duty_u16(Null_X)
    tilt.duty_u16(Null_Y)
    time.sleep(1)
    pan.deinit()
    tilt.deinit()