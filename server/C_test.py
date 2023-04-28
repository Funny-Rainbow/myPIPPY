import asyncio
import websockets #tcp
#socket udp
#admin:123456
async def hello(Str):
    async with websockets.connect("ws://192.168.43.127:8888") as websocket:
        await websocket.send("admin:123456")
        await websocket.send(Str)
        me = await websocket.recv()
        print('Server Reply:', me)


if __name__ == "__main__":
    while True:
        str = input('Input your code:\n')
        asyncio.run(hello(str))