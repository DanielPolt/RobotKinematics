import time
import servos
robot = servos.robot
print("Set value for X")
xinput = float(input())
print("Set value for Y")
yinput = float(input())
ips = xinput / yinput
distance = 0
if abs(ips) > robot.leftmaxips or abs(ips) < robot.leftminips:
    print("Impossible movement")
else:
    tenseconds = time.monotonic()
    starttime = time.monotonic()
    robot.resetCounts()
    robot.setSpeedsIPS(ips, ips)
    while distance < abs(xinput):
        elapsedtime = time.monotonic() - starttime
        if elapsedtime > 1 :
            print(robot.getSpeeds(robot.getCounts(), 1))
            starttime = time.monotonic()
        distance = (robot.getCounts()[1] / 32) * servos.CIRCUMFERENCE
    robot.setSpeedsPWM(1.5,1.5)
    while time.monotonic() - tenseconds < 10:
        print(robot.getSpeeds(robot.getCounts(), 1))
        time.sleep(1)
        
        