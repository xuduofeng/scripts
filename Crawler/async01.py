__author__ = 'derek'
import asyncio
from aiohttp import ClientSession
from datetime import datetime

async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            delay = response.headers.get("DELAY")
            date = response.headers.get("DATE")
            print("{}:{} with delay {}".format(date, response.url, delay))
            return await response.read()


async def run(loop, r):
    #url = "http://192.168.11.8:8080/{}"
    url = "http://localhost:8080/{}"
    tasks = []
    for i in range(r):
        task = asyncio.ensure_future(fetch(url.format(i)))
        tasks.append(task)
        #print(i)
        #print(datetime.now())
    responses = await asyncio.gather(*tasks)
    #print(responses)


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(loop, 100))
loop.run_until_complete(future)
loop.close()


#loop.run_until_complete(run(loop, 100))