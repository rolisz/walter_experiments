def changeSpeed(startSpeed, endSpeed, jerk=1.0):
    changeSign = False
    if startSpeed > endSpeed:
        changeSign = True
        startSpeed, endSpeed = endSpeed, startSpeed
    accel = 0
    speeds = []
    
    while startSpeed < endSpeed/2:
        accel+=jerk
        startSpeed += accel
        speeds.append(startSpeed)

    while startSpeed < endSpeed and accel > 0:
        accel-=jerk
        startSpeed += accel
        speeds.append(startSpeed)
        
    if changeSign:
        speeds.reverse()
    return speeds
        
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def getSpeeds(fromSpeed, toSpeed, steps):
    ratio = (toSpeed - fromSpeed) / (sigmoid(5) - sigmoid(-5))
    offset = fromSpeed
    speeds = []
    x = -5
    while x<=5:
        x+= 10.0 / steps
        speeds.append(offset+ratio*sigmoid(x))
    return speeds
def drive(x):
    print x

a = getSpeeds(0, 100, 20)
b = changeSpeed(0, 100, 1)

for x, y in zip(a, b):
    print x, y
    
#TODO: compare
