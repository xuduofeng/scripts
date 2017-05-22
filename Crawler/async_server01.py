__author__ = 'derek'
import asyncio
from datetime import datetime
from aiohttp import web
import random


async def hello(request):
    name = request.match_info.get("name", "foo")
    date = datetime.now().isoformat()
    delay = random.randint(0, 3)
    await asyncio.sleep(delay)
    headers = {"content_type":"text/html","delay":str(delay)}

    with open("frank.html", "rb") as html_body:
        print("{}: {} delay: {}".format(date, request.path, delay))
        response = web.Response(body=html_body.read(), headers=headers)
        return response

app = web.Application()
app.router.add_route("GET", "/{name}", hello)
web.run_app(app)