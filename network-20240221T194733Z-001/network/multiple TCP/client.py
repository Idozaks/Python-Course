import socket

MAX_MSG_LENGTH = 1024
SERVER_IP = '127.0.0.1'
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_IP, PORT))
    while True:
        pass
