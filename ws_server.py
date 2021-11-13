import asyncio
import websockets
import scraper

HOST = "localhost"
PORT = 5051

async def rcv_and_send(websocket, ws):
    json_url = await websocket.recv()
    print(f"Got JSON: {json_url}")

    # Get the URL from the JSON provided
    url = scraper.JSONtoURL(json_url)
    print(f"URL: {url}")

    # Get list of images from URL
    image_list = scraper.scrape_site(url)
    print(f"Image list: {image_list}")

    # Convert image list to JSON
    response = scraper.LISTtoJSON(image_list)
    print(f"Sending response: {response}")

    await websocket.send(response)

async def main():
    async with websockets.serve(rcv_and_send, HOST, PORT):
        await asyncio.Future()  # run forever

print(f"Websocket server listening on {HOST} at port {PORT}")
asyncio.run(main())