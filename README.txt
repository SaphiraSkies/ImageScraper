===== CS 361 Image Scraper Microservice =====

Description:

The image scraper microservice currently runs by connecting to a local host on port 5050.

It works like this:
1. Server runs, listening for socket connections.
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

Note: It is important to send both the message length and the message itself in order to ensure all data is received accurately.

************************************

To run the Image Scraper service:
1. Clone/download repository
2. Install dependencies:
	pip install requests
	pip install beautifulsoup4
3. Run:
	python3 server.py

************************************

To run the test client:
1. Run:
	python3 client.py