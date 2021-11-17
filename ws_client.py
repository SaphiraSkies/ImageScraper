###################################################################################
# Hannah Moon - Image Scraper Microservice - Websocket Client
# 11/11/2021
# This service runs a server which will take a JSON input for a URL
# and return a JSON list of image URLs for download. It connects via websockets.
###################################################################################

import asyncio
import websockets

HOST = "localhost"
PORT = 5051

# Client sends a URL JSON to server, then waits for response
async def run_ws():
    uri = "ws://" + HOST + ":" + str(PORT)
    async with websockets.connect(uri) as websocket:
        test_url = '{"URL":"https://en.wikipedia.org/wiki/Rat"}'

        await websocket.send(test_url)
        print(f"Sent to server: {test_url}")

        response = await websocket.recv()
        print(f"Response: {response}")

asyncio.run(run_ws())