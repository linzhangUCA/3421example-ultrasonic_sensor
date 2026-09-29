from machine import Pin, PWM, reset
from time import ticks_us

class DistanceSensor:
    def __init__(self, trig_id, echo_id, trig_freq=12):
        self.trig_pin = PWM(Pin(trig_id), freq=trig_freq, duty_ns=10_000)
        self.echo_pin = Pin(echo_id, Pin.IN, Pin.PULL_DOWN)
        self.echo_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self.calc_dist)
        self.distance = None
        self.echo_up_instant = None

    def calc_dist(self, pin):
        if pin.value():  # echo pin pulled up
            self.echo_up_instant = ticks_us()
        else:  # echo pulled down
            dt = ticks_us() - self.echo_up_instant
            if dt < 100:  # too short, may be a mis-detection
                self.distance = 0.0
            elif 100 <= dt < 38000:
                self.distance = 343 * dt * 1e-6 * 0.5  # v(m/s) * t (s) / 2
            else:  # out of range
                self.distance = None

if __name__ == "__main__":
    from time import sleep_ms

    # SETUP
    sensor = DistanceSensor(trig_id=3, echo_id=2, trig_freq=15)

    # LOOP
    while True:
        print(f"Distance: {sensor.distance} m")
        sleep_ms(200)
