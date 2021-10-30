#!/usr/bin/env python3
from pysbus import *


async def rc():
    sbus = await SBUSReceiver.create("/dev/ttyUSB0")
    while True:
        frame = await sbus.get_frame()
        print(frame)

loop = asyncio.get_event_loop()
loop.run_until_complete(rc())
loop.run_forever()
loop.close()
