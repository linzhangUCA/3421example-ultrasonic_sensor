from machine import Pin
from time import sleep_us, sleep_ms, ticks_us

# SETUP
trig = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN, Pin.PULL_DOWN)
# Config IRQ
tic, toc, distance = None, None, None
def resolve_status(pin):
    global tic, toc, distance
    if pin.value():
        tic = ticks_us()
    else:
        dt = ticks_us() - tic
        if dt < 100:
            distance = 0.
        elif 100 <= dt < 38000:
            distance = dt / 58 / 100
        else:
            distance = None
echo.irq(handler=resolve_status)

# LOOP
while True:
    trig.on()
    sleep_us(10)
    trig.off()  # 10 us pulse to trigger
    print(f"distance: {distance} m")
    sleep_ms(60)

