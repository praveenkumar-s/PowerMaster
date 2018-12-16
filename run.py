import time
import pigpio
from datetime import datetime

import subprocess
from datetime import datetime
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler

import json
try:
    import asyncio
except ImportError:
    import trollius as asyncio





timediff=datetime.now()
counter=0
IMP=0

# 1200 imp / hour 
# current wattage usage = 3600/ (time interval * 1200)
#call back function, that gets triggered every time there is a pulse
def cbf(gpio, level, tick):
    global IMP
    IMP=IMP+1
    print("{:2d}->{} at {}".format(gpio, level, tick))
    
GPIO=15
GLITCH=500
SLEEP=60

pi = pigpio.pi()

if not pi.connected:
   exit(0)

pi.set_mode(GPIO, pigpio.INPUT)

# Ignore edges shorter than GLITCH microseconds.
pi.set_glitch_filter(GPIO, GLITCH)

cb = pi.callback(GPIO, pigpio.FALLING_EDGE, cbf)


print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

# Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
try:
    asyncio.get_event_loop().run_forever()
except (KeyboardInterrupt, SystemExit):
    pass