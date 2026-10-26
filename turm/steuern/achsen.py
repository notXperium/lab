from machine import Pin, PWM, ADC, I2C
from machine_i2c_lcd import I2cLcd
import time

pan = PWM(Pin(21), freq=50)
tilt = PWM(Pin(15 ), freq=50)

# i2c = I2C(0, sda=Pin(13), scl=Pin(14), freq=400000)
# lcd = I2cLcd(i2c, 0x27, 2, 16)  

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

# def zeige(zeile, text):
#     lcd.move_to(0, zeile)
#     lcd.putstr((text + " " * 16)[:16])

Null_X = duty(0)
Null_Y = duty(0)

# lcd.clear()
pan.duty_u16(Null_X)
tilt.duty_u16(Null_Y)
# zeige(0, "Turm bereit")
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
            # zeige(0, "Ausgangsposition")
            # zeige(1, "")
        else:
            x = winkel_X(VRx.read())
            y = winkel_Y(VRy.read())
            if abs(x- oldX) > 1.0: 
                pan.duty_u16(duty(x))
                oldX = x
            if abs(y - oldY) > 1.0:
                tilt.duty_u16(duty(y))
                oldY = y

            # zeige(0, "Pan:  " + str(round(x)) + " Grad")
            # zeige(1, "Tilt: " + str(round(y)) + " Grad")

        time.sleep(0.02)
finally:
    pan.duty_u16(Null_X)
    tilt.duty_u16(Null_Y)
    # zeige(0, "Ausgangsposition")
    # zeige(1, "Turm aus")
    time.sleep(1)
    pan.deinit()
    tilt.deinit()