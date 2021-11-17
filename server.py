###################################################################################
# Hannah Moon - Image Scraper Microservice - Python Server
# 11/8/2021
# This service runs a server which will take a JSON input for a URL
# and return a JSON list of image URLs
###################################################################################

# The following references were used:
# https://www.youtube.com/watch?v=3QiPPX-KeSc
# https://www.youtube.com/watch?v=Lbfe3-v7yE0&t=67s
# https://www.youtube.com/watch?v=stIxEKR7o-c&t=33s&ab_channel=JohnWatsonRooney

import socket
import scraper

HEADER = 64
PORT = 5050
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "/q"

# Connect socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
running = True

url = '"URL"'

# This function formats a message to send to client,
# letting it know how long of a message to expect first
def send(msg, conn):
    # Encode the message and get its length
    message = msg.encode(FORMAT)
    msg_length = len(message)                                   # msg_length is an int
    send_length = str(msg_length).encode(FORMAT)                # send_length turns msg_length to a str and encodes it
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)

# Client connects, and a message confirms
def handle_client(conn, addr):
    print(f"Server connected to client {addr}.")

    # While the connection is running...
    connected = True
    while connected:
        print("Waiting on client...")
        # First receive the upcoming message's expected length
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # If a message is incoming...
        if msg_length:
            # Convert it to int
            msg_length = int(msg_length)
            # Receive message of that expected length
            msg = conn.recv(msg_length).decode(FORMAT)

            # Disconnect if this is a "quit" message
            if msg == DISCONNECT_MESSAGE:
                print("Client disconnected.")
                conn.close()
                connected = False
                return

            # Print received message
            print(f"Received from client: {msg}")

            # If this is looking for an image from a website URL...
            if url in msg:
                sendmsg = scraper.LISTtoJSON(scraper.scrape_site(scraper.JSONtoURL(msg)))
                send(sendmsg, conn)
                print("Sending list back:")
                print(f"{sendmsg}")
            else:
                print("Error reading URL from JSON.")

    conn.close()

# Starts server listening for connections
server.listen()
print(f"Python server is listening on {SERVER}, port {PORT}")

# Waits for connection
while running:
    conn, addr = server.accept()
    handle_client(conn, addr)
    running = False