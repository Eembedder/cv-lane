
from controllers import *
import time

car_controller = Controller()

# Motor values are in range 0 <= x <= 100
print('Turning left')
for i in range(0, 10):
    car_controller.turn(10*i, left=True)
    time.sleep(0.5)

print('Turning right')
for i in range(0, 10):
    car_controller.turn(10*i, left=False)
    time.sleep(0.5)

car_controller.straighten()
