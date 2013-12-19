from ssc32 import *
from time import sleep
from smooth import getPositions
# Run with sudo
ssc = SSC32('/dev/ttyUSB0', 115200)
ssc[0].degrees = 20
ssc[0].max = 2500
ssc[0].min = 500
ssc[0].deg_max = +90.0
ssc[0].deg_min = -90.0

#TODO: fix library so it doesn't take 100ms for the first instruction
# And which overrides the current command even if it has the same targetDegs

def moveTo(motor, mi, time, targetDegs, dryRun=True):
    currDegs = motor[mi].degrees
    motor[mi].degrees = targetDegs
    if dryRun:
        print time, motor[mi].degrees
    else:
        motor.commit(time*1000)
    sleep(time)

def smoothMoveTo(motor, mi, time, targetDegs, dryRun=True):
    freq = 100.0
    timePerStep = time/freq
    currDegs = motor[mi].degrees
    distToGo = targetDegs - currDegs
    for pos in getPositions(currDegs, targetDegs, freq):
        moveTo(motor, mi, timePerStep, pos, dryRun)
    
    
#elbow: 35 -> -100

#ssc[0].degrees = 0
#ssc.commit(4000)
ssc[0].degrees = -30
ssc.commit(1000)
x=-30
while True:
    k = raw_input()
    if x < 30:
        x = 30
        moveTo(ssc, 0, 1, x, True)
    else:
        x = -30
        smoothMoveTo(ssc, 0, 1, x, True)

ssc.close()
#
#minus = -1
#while True:
#    ssc[0].degrees = minus * 20
#    ssc.commit()
#    minus *= -1
#    sleep(4)
