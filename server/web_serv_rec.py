import websockets
import asyncio



async def main(url):
    async with websockets.serve(echo,'localhost',1313):
        await asyncio.Future() # run forever