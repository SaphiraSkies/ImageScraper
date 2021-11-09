###################################################################################
# Hannah Moon - Image requesting client
# 11/8/2021
# This is a test client for the image scraper microservice.
###################################################################################

# The following references were used:
# https://www.youtube.com/watch?v=3QiPPX-KeSc
# https://www.youtube.com/watch?v=Lbfe3-v7yE0&t=67s

import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "/q"
SERVER = 'localhost'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connected = False

test_URL = "https://www.allrecipes.com/search/results/?search=chocolate+pancakes"
test_keyword = "pikachu"
num_images = 3

def URLtoJSON(str):
    return '{"URL": "' + str + '"}'

def KEYtoJSON(str):
    return '{"keyword": "' + str + '"}'

# Attempt to connect to server
try:
    client.connect(ADDR)
    connected = True
    print(f"Client connected to {SERVER}, on port {PORT}")
except:
    print("ERROR connecting client to server.")

# This function formats a message to send to server,
# letting it know how long of a message to expect first
def send(msg):
    # Encode the message and get its length
    message = msg.encode(FORMAT)
    msg_length = len(message)                                   # msg_length is an int
    send_length = str(msg_length).encode(FORMAT)                # send_length turns msg_length to a str and encodes it
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

# While connected to server...
while connected:
    # Send a stringified JSON
    # msg = KEYtoJSON(test_keyword)       # Test a keyword
    msg = URLtoJSON(test_URL)         # Test a URL
    send(msg)

    print(f"Sent message to server: {msg}")
    print("Waiting for response...")

    # Block here, wait for a response...
    # Receive message size first
    msg_length = client.recv(HEADER).decode(FORMAT)
    if msg_length:
        # Convert it to int
        msg_length = int(msg_length)
        # Receive message of that expected length
        msg = client.recv(msg_length).decode(FORMAT)

        # Show the received message
        print(f"Received from server: \n{msg}")

        # Tell server to disconnect
        print("Client disconnecting from server.")
        send("/q")
        connected = False