import asyncio
import websockets



async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)
        print('Client message:', message)

async def main():
    async with websockets.serve(echo, "127.0.0.1", 1025):
        await asyncio.Future()  # run forever

#

asyncio.run(main())