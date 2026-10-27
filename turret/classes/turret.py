from machine import PWM, Pin

class Turret:
    def __init__(self, pan_PIN, tilt_PIN):
        self.pan_PIN = PWM(Pin(pan_PIN), freq=50)
        self.tilt_PIN = PWM(Pin(tilt_PIN), freq=50)

        self.nullPan = 0
        self.nullTilt = 0

    def duty(self, w):
        ms = 1/90*w + 0.5
        return int(ms/20 * 65535)


    def aim(self, pan, tilt):
        if 0 <= pan <= 180 and 0 <= tilt <= 180:
                self.pan_PIN.duty_u16(self.duty(pan))
                self.tilt_PIN.duty_u16(self.duty(tilt))
        else: raise ValueError("pan and tilt must be 0-180")
