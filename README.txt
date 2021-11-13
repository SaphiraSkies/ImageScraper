===== CS 361 Image Scraper Microservice =====
Hannah Moon
CS361

Description:

The image scraper microservice has two options: One for connecting via python sockets, a second for connecting via websockets.

The PYTHON socket connects to a local host on port 5050.
The JS socket connects to a local host on port 5051.

************************************

PYTHON connection works like this:
1. Server runs, listening on port 5050.
2. Client runs, attempts to connect.
3. Server accepts connection and waits for a message from client.
4. Client needs to send two messages: first one with the length of the message to send (in bytes), then followed by the actual message.
5. Server receives two messages: the length (in bytes) of the message, then the message itself.
	The server expects to receive a stringified JSON in this format:
	{"URL": "http://www.google.com"}
6. The server will scrape images from the given URL.
7. The server then sends back the message length (in bytes) and the message itself. It is a stringified JSON in this format:
	{"URL": [
		http://www.website.com/cupcake.jpg,
		http://www.website.com/soup.jpg,
		http://www.website.com/tea.jpg,
		]}
8. The client receives the message length, then the message.
9. The client will need to sort and handle the JSON results.

************************************

JS WEBSOCKETS connection works like this:
1. Server runs, listening on port 5051.
2. Client runs, attempts to connect.
3. Server listens for a message.
4. Client sends a url in JSON format. (e.g. {"URL": "http://www.example.com")
5. Server responds with a JSON list of images. (e.g. {"URL": [image1.png, image2.png]})
6. The client will need to sort and handle the JSON results.

Note: It is important to send both the message length and the message itself in order to ensure all data is received accurately.

************************************

To run the Image Scraper service:
1. Clone/download repository
2. Install dependencies:
	pip install requests
	pip install beautifulsoup4
	pip install websockets
3a. To run the server for PYTHON sockets:
	python3 server.py
3b. To run the server for JS websockets:
	python3 ws_server.py

************************************

To run the test client:
1a. Run for PYTHON sockets:
	python3 client.py
1b. Run for JS websockets:
	python3 ws_client.py

************************************

Running on flip:
If you need to run the service on the flip server and have not done so before,
you may need to set up the virtual environment first.

1. Copy the python files to a folder on the server (example: moonha/CS361/imagescraper)
2. Navigate to that folder: cd imagescraper
3. Create venv for the folder: virtualenv imagescraper
4. Activate the venv: source imagescraper/bin/activate
5. Install dependencies using:
	pip3 install requests
	pip3 install beautifulsoup4
	pip3 install websockets
6. You should now be able to run the scraper server: python3 server.py
7. You can deactivate the venv: deactivate