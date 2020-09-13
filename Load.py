import servos
import time
robot = servos.robot
f = open("load.txt", "w")
loads = 3
while loads > 0:
    robot.setSpeedsPWM(1.6, 1.6)
    t1 = time.monotonic()
    while time.monotonic() - t1 < 10: #get data for 10 seconds on one surface
        f.write(str(robot.getSpeeds()))
        f.write("\n")
    robot.setSpeedsPWM(1.5, 1.5)
    time.sleep(5) #move robot
    loads -= 1 #3 different surfaces
robot.setSpeedsPWM(1.5, 1.5)
f.close()