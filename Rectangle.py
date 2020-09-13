import time
import servos
robot = servos.robot
print("Set value for H")
hinput = float(input())
print("Set value for W")
winput = float(input())
print("Set value for Y")
yinput = float(input())
distance = 0
rotated = 0
rotationlength = (3.14 / 2) * servos.DMID
rotations = rotationlength / servos.CIRCUMFERENCE
constantspeed = ((2 * hinput) + (2 * winput) + (3 * (rotationlength))) / yinput
turn90 = (3.14 / 2) / (constantspeed / rotationlength)
if constantspeed > robot.leftmaxips or constantspeed < robot.leftminips:
    print("Impossible movement")
else:
    robot.resetCounts()
    robot.setSpeedsIPS(constantspeed, constantspeed)
    while distance < hinput :
        distance = (robot.getCounts()[1] / 32) * servos.CIRCUMFERENCE
    robot.setSpeedsPWM(1.5, 1.5)
    distance = 0
    robot.resetCounts()
    robot.setSpeedsVW(0, turn90)
    while rotated < rotations:
        rotated = robot.getCounts()[0] / 32
    robot.setSpeedsPWM(1.5, 1.5)
    rotated = 0
    robot.resetCounts()
    robot.setSpeedsIPS(constantspeed, constantspeed)
    while distance < winput:
        distance = (robot.getCounts()[1] / 32) * servos.CIRCUMFERENCE
    robot.setSpeedsPWM(1.5, 1.5)
    distance = 0
    robot.resetCounts()
    robot.setSpeedsVW(0, turn90)
    while rotated < rotations:
        rotated = robot.getCounts()[0] / 32
    robot.setSpeedsPWM(1.5, 1.5)
    rotated = 0
    robot.resetCounts()
    robot.setSpeedsIPS(constantspeed, constantspeed)
    while distance < hinput:
        distance = (robot.getCounts()[1] / 32) * servos.CIRCUMFERENCE
    robot.setSpeedsPWM(1.5, 1.5)
    distance = 0
    robot.resetCounts()
    robot.setSpeedsVW(0, turn90)
    while rotated < rotations:
        rotated = robot.getCounts()[0] / 32
    robot.setSpeedsPWM(1.5, 1.5)
    rotated = 0
    robot.resetCounts()
    robot.setSpeedsIPS(constantspeed, constantspeed)
    while distance < winput:
        distance = (robot.getCounts()[1] / 32) * servos.CIRCUMFERENCE
    robot.setSpeedsPWM(1.5, 1.5)
    distance = 0
    robot.resetCounts()
robot.setSpeedsPWM(1.5, 1.5)
        
    