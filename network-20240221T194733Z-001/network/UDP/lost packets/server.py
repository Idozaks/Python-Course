import random
import socket

SERVER_IP = '0.0.0.0'
PORT = 8821
MAX_MSG_SIZE = 1024

bank_balance = 1000


def special_sendto(socket_object, response, client_address):
    fail = random.randint(1, 3)
    if not (fail == 1):
        socket_object.sendto(response.encode(), client_address)
    else:
        print("Oops")


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((SERVER_IP, PORT))
    print('server running')
    while True:
        (client_message, client_address) = server_socket.recvfrom(MAX_MSG_SIZE)
        data = client_message.decode()[4:]
        serial_number = client_message.decode()[:4]
        if data.lower() == 'exit':
            break
        if data.lower() == 'pay':
            bank_balance -= 1000
            special_sendto(server_socket, serial_number + '')
    print('closing server')