import pigpio
from apscheduler.schedulers.asyncio import AsyncIOScheduler


try:
    import asyncio
except ImportError:
    import trollius as asyncio

    
def cbf(gpio, level, tick):
       print(gpio, level, tick)


GPIO=15
GLITCH=500
SLEEP=60

pi = pigpio.pi()

pi = pigpio.pi()

if not pi.connected:
   exit(0)
pi.set_mode(GPIO, pigpio.INPUT)

pi.set_glitch_filter(GPIO, GLITCH)


cb = pi.callback(GPIO, pigpio.FALLING_EDGE, cbf)

try:
    asyncio.get_event_loop().run_forever()
except (KeyboardInterrupt, SystemExit):
    pass