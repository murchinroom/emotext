# API server for the emotext
# PYTHONPATH=$PYTHONPATH:. python emotext/httpapi.py

import asyncio
import argparse
from datetime import datetime

from aiohttp import web

from emotext import *


class EmotextServer:
    """POST / with text/plain body to get the emotion count of the text.

    Example:

        curl -X POST localhost:8080/ --data '高兴'

    """

    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.emotext = Emotions()

    async def start(self):
        app = web.Application()
        app.add_routes([web.post('/', self.handle)])
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, self.host, self.port)
        await site.start()
        print(f'Emotext server started at http://{self.host}:{self.port}')
        while True:
            await asyncio.sleep(3600)

    async def handle(self, request: web.Request):
        text = await request.text()
        result = self.emotext.emotion_count(text)

        # access log
        print(
            f'[HTTP] {datetime.now()}: {request.remote} {request.method} {request.path} {text=}')

        result_emotions = {key: value for key,
                           value in result.emotions.items() if value != 0}
        result_polarity = {key.name: value for key,
                           value in result.polarity.items() if value != 0}
        va = result.emotions_va() or [None, None]
        result_va = {"valence": va[0], "arousal": va[1]}
        return web.json_response({
            'emotions': result_emotions, 
            'polarity': result_polarity,
            'va': result_va})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost',
                        type=str, help='host to listen on. (default: localhost)')
    parser.add_argument('--port', default=8080, type=int,
                        help='port to listen on. (default: 8080)')
    args = parser.parse_args()

    server = EmotextServer(host=args.host, port=args.port)
    asyncio.run(server.start())
