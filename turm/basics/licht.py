from machine import Pin, PWM

led = PWM(Pin(2), freq=1000)
led.duty_u16(65535)