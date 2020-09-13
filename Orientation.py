import servos
import time
robot = servos.robot
print("Set value for X")
xinput = float(input())
print("Set value for Y")
yinput = float(input())
xinputrad = xinput * (3.14159 / 180) * -1 #convert to radians and make counterclockwise
angularvelocity = xinputrad / yinput
arclength = xinputrad * servos.DMID
rrotations = arclength / servos.CIRCUMFERENCE
lrotations = rrotations
rspeed = rrotations / yinput
lspeed = -1 * rspeed
rotated = 0
robot.resetCounts()
if abs(lspeed) > robot.leftmaxrps or abs(lspeed) < robot.leftminrps:
    print("Impossible movement")
else:
    starttime = time.monotonic()
    robot.setSpeedsVW(0, angularvelocity)
    while rotated < abs(lrotations):
        elapsedtime = time.monotonic() - starttime
        if elapsedtime > 1:
            print(robot.getSpeeds(robot.getCounts(), 1))
            starttime = time.monotonic()
        rotated = robot.getCounts()[0] / 32
robot.setSpeedsPWM(1.5, 1.5)

