# 3421example-ultrasonic_sensor
[HC-SR04](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf) usage examples 

## 1 Wiring
### 1.1 Powered by Pico's Micro-USB Connection
![wiring-usb](images/hcsr04_wiring-usb.png)

### 1.2 Powered by External 5V Source (e.g. Buck Converter)
![wiring-peb](images/hcsr04_wiring-peb.png)

## 2 Usage
Just want to have some fun with the sensor? 
Run [basic_ranging.py](basic_ranging.py) using MicroPython and Pico.
> [!NOTE]
> Check wiring!

If distance sensor is required by other project, upload [distance_sensor.py](distance_sensor.py) to Pico.
Then, import the `DistanceSensor` class when needed.
```python
from distance_sensor import DistanceSensor
dsensor_instance = DistanceSensor(trig_id=3, echo_id=2)  # make sure pin ids match your wiring 
```