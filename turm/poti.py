from machine import Pin, PWM, ADC

led = PWM(Pin(2), freq=1000)

poti = ADC(Pin(1))
poti.atten(ADC.ATTN_11DB)

def lies():
    inp = []

    for _ in range(16):
        inp.append(poti.read())
    return sum(inp)//len(inp)

def duty(wert):
    anteil = wert / 4095
    return int(anteil * 65535)

while True:
    led.duty_u16(duty(lies()))


