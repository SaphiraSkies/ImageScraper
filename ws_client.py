import asyncio
import websockets

HOST = "localhost"
PORT = 5051

async def run_ws():
    uri = "ws://" + HOST + ":" + str(PORT)
    async with websockets.connect(uri) as websocket:
        test_url = '{"URL":"https://en.wikipedia.org/wiki/Rat"}'

        await websocket.send(test_url)

        response = await websocket.recv()
        print(f"Response: {response}")

asyncio.run(run_ws())