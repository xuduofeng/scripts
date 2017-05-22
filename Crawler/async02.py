__author__ = 'derek'
import asyncio
import threading

@asyncio.coroutine
def hello():
    print("hello world! (%s)" % threading.currentThread())

    yield from asyncio.sleep(3)
    #await asyncio.sleep(2)
    print("hello again! (%s)" % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()