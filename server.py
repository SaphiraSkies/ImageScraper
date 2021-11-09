###################################################################################
# Hannah Moon - Image Scraper Microservice
# 11/8/2021
# This service runs a server which will take a JSON input for a URL or keyword
# and return a JSON list of image URLs for download
###################################################################################

# The following references were used:
# https://www.youtube.com/watch?v=3QiPPX-KeSc
# https://www.youtube.com/watch?v=Lbfe3-v7yE0&t=67s

import socket

HEADER = 64
PORT = 5050
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "/q"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

running = True

url = '"URL"'
keyword = '"keyword"'

example_list = [
    "https://secure.img1-fg.wfcdn.com/im/77981853/resize.jpg",
    "https://cdn.vox-cdn.com/thumbor/eFEHo8eygHajtwShwT9e.jpeg",
    "https://static0.gamerantimages.com/wordpress/wp-content/uploads/2021/09/Pokemon-GO-Pikachu.jpg"
]

# Formats a list as a JSON string
def LISTtoJSON(list):
    str_list = "["
    str_list = str_list + ', '.join(list)
    str_list = str_list + "]"
    return '{"URL": ' + str_list + '}'

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

            # Print received message
            print(f"Received from client: {msg}")

            # If this is looking for an image from a website URL...
            if url in msg:
                print("Grabbing images from URL...")
                sendmsg = LISTtoJSON(example_list)
                send(sendmsg, conn)
                print("Sending list back:")
                print(f"{sendmsg}")
                pass

            # If this is looking for an image from a keyword in Google images...
            if keyword in msg:
                print("Grabbing top 3 images from Google...")
                sendmsg = LISTtoJSON(example_list)
                send(sendmsg, conn)
                print("Sending list back:")
                print(f"{sendmsg}")
                pass

            # Disconnect if this is a "quit" message
            if msg == DISCONNECT_MESSAGE:
                print("Client disconnected.")
                conn.close()
                connected = False
                return

    conn.close()

# Starts server listening for connections
server.listen()
print(f"Server is listening on {SERVER}, port {PORT}")

# Waits for connection
while running:
    conn, addr = server.accept()
    handle_client(conn, addr)
    running = False