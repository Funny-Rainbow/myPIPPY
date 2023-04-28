import websockets
import asyncio


async def hello():
    url = 'ws://127.0.0.1:1313'
    async with websockets.connect(url) as websocket:
        name = input('What is your name')

        await websocket.send(name)
        print(name)

        greeting = await websocket.recv()
        print(greeting)

if __name__ == '__main__':
    asyncio.run(hello())