from distance_sensor import DistanceSensor
from time import sleep_ms
from machine import reset

# SETUP
sensor = DistanceSensor(trig_id=18, echo_id=19)

# LOOP
try:
    while True:
        print(f"Distance: {sensor.distance} m")
        sleep_ms(200)
except KeyboardInterrupt:
    reset()