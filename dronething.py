from time import sleep

from djitellopy import Tello

tello = Tello()
# movements are in cenimeters sleep is in seconds
tello.takeoff()

sleep(1)
tello.move_up(76)

sleep(1)
tello.move_forward(305)

sleep(1)
tello.move_left(305)

sleep(1)
tello.move_back(305)

sleep(1)
tello.move_right(305)

sleep(1)
tello.flip_forward()

sleep(1)
tello.land()
tello.end()
