#Task 1.12
import time
import servos
robot = servos.robot
f = open("PWMdata.txt", "w")
leftwheelPWM = 1.3
rightwheelPWM = 1.3
leftwheelRPS = 0
rightwheelRPS = 0
f.write("Left\n")
while leftwheelPWM <= 1.7:
    robot.setSpeedsPWM(leftwheelPWM, 1.5)
    time.sleep(1)
    robot.resetCounts()
    time.sleep(3)
    leftwheelRPS = (robot.getCounts()[0]/ 32) / 3
    f.write(str(leftwheelPWM))
    f.write(",")
    f.write(str(leftwheelRPS))
    f.write("\n")
    leftwheelPWM = round(leftwheelPWM + 0.01, 2)
f.write("Right\n")
while rightwheelPWM <= 1.7:
    robot.setSpeedsPWM(1.5, rightwheelPWM)
    time.sleep(1)
    robot.resetCounts()
    time.sleep(3)
    rightwheelRPS = (robot.getCounts()[1]/ 32) / 3
    f.write(str(rightwheelPWM))
    f.write(",")
    f.write(str(rightwheelRPS))
    f.write("\n")
    rightwheelPWM = round(rightwheelPWM + 0.01, 2)
robot.setSpeedsPWM(1.5, 1.5)
f.close()
    
    