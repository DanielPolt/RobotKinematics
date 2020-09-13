import servos
import time
robot = servos.robot
print("Set value for R")
rinput = float(input())
print("Set value for Y")
yinput = float(input())
distanceouter = 0
rotated = 0
rotationlength = 3.14 * servos.DMID
rotations = rotationlength / servos.CIRCUMFERENCE
constantspeed = (((3.14 * rinput) * 2) + rotationlength)/ yinput
print(constantspeed)
angularvelocity = constantspeed / rinput
print(angularvelocity)
turn180 = 3.14 / (constantspeed / rotationlength)
if constantspeed > robot.leftmaxips or constantspeed < robot.leftminips:
    print("Impossible movement")
else:
    robot.resetCounts()
    robot.setSpeedsVW(constantspeed, angularvelocity)
    while distanceouter < (3.14159 * (rinput + servos.DMID)):
        distanceouter = (robot.getCounts()[0] / 32) * servos.CIRCUMFERENCE
    robot.setSpeedsPWM(1.5, 1.5)
    distanceouter= 0
    robot.resetCounts()
    robot.setSpeedsVW(0, turn180)
    while rotated < rotations:
        rotated = robot.getCounts()[0] / 32
    robot.setSpeedsPWM(1.5, 1.5)
    rotated = 0
    robot.resetCounts()
    robot.setSpeedsVW(constantspeed, (angularvelocity * -1))
    while distanceouter < (3.14159 * (rinput + servos.DMID)):
        distanceouter = (robot.getCounts()[1] / 32) * servos.CIRCUMFERENCE
    distanceouter = 0
    robot.resetCounts()
robot.setSpeedsPWM(1.5, 1.5)
