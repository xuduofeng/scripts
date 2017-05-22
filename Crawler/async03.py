#!/usr/bin/env python3
__author__ = 'derek'

import asyncio
from aiohttp import ClientSession

async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            delay = response.headers.get("DELAY")
            date = response.headers.get("DATE")
            print("{}:{} with delay {}".format(date, response.url, delay))
            return await response.read()


async def bound_fetch(sem, url):
# getter function with semaphore
  async with sem:
    await fetch(url)


async def run(loop, r):
    url = "http://192.168.11.8:8080/{}"
    tasks = []
    sem = asyncio.Semaphore(1000)
    for i in range(r):
        task = asyncio.ensure_future(bound_fetch(sem, url.format(i)))
        tasks.append(task)
    responses = await asyncio.gather(*tasks)
        #print(responses)


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(loop, 10000))
loop.run_until_complete(future)