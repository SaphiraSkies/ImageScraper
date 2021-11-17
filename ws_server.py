###################################################################################
# Hannah Moon - Image Scraper Microservice - Websocket Server
# 11/11/2021
# This service runs a server which will take a JSON input for a URL
# and return a JSON list of image URLs for download. It connects via websockets.
###################################################################################

import asyncio
import websockets
import scraper

HOST = "localhost"
PORT = 5051

# This function takes a websocket connection, then receives
# a JSON URL from the client, and sends back a JSON formatted
# list of image URLS
async def rcv_and_send(websocket, ws):
    json_url = await websocket.recv()
    print(f"Got JSON: {json_url}")

    # Get the URL from the JSON provided
    url = scraper.JSONtoURL(json_url)
    print(f"URL: {url}")

    # Get list of images from URL
    image_list = scraper.scrape_site(url)
    print(f"\nImage list: {image_list}")

    # Convert image list to JSON
    response = scraper.LISTtoJSON(image_list)
    print(f"\nSending response: {response}")

    await websocket.send(response)

# Runs the server
async def main():
    async with websockets.serve(rcv_and_send, HOST, PORT):
        await asyncio.Future()  # run forever

print(f"Websocket server listening on {HOST} at port {PORT}")
asyncio.run(main())