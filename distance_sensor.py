from machine import Pin, PWM, reset

class DistanceSensor:
    def __init__(self, trig_id, echo_id):
        self.trig_pin = PWM(Pin(trig_id), freq=12, duty_ns=10_000)
        self.echo_pin = Pin(echo_id, Pin.IN, Pin.PULL_DOWN)
        self.echo_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._echo_handler)
        self._distance = None
        self._start_time = None

    def distance(self):
        return self._distance

    def _echo_handler(self, pin):
        if pin.value():
            self._start_time = ticks_us()
        else:
            dt = ticks_us() - self._start_time
            if dt < 100:
                self._distance = 0.0
            elif 100 <= dt < 38000:
                self._distance = dt / 58 / 100
            else:
                self._distance = None

if __name__ == "__main__":
    from time import sleep_ms, ticks_us

    sensor = DistanceSensor(trig_id=3, echo_id=2)

    try:
        while True:
            print(f"Distance: {sensor.distance()} m")
            sleep_ms(200)
    except KeyboardInterrupt:
        reset()