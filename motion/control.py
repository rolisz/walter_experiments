from ssc32 import *
from time import sleep
ssc = SSC32('/dev/ttyUSB0', 115200)
ssc[0].degrees = 20
ssc[0].max = 2500
ssc[0].min = 500
ssc[0].deg_max = +90.0
ssc[0].deg_min = -90.0

ssc[0].degrees = 0
ssc.commit(4000)
sleep(1)
ssc[0].degrees = 0
ssc.commit(500)

ssc.commit(time=20000)
ssc.close()
#
#minus = -1
#while True:
#    ssc[0].degrees = minus * 20
#    ssc.commit()
#    minus *= -1
#    sleep(4)
