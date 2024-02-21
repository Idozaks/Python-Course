import random
import socket

SERVER_IP = '127.0.0.1'
PORT = 8821
MAX_MSG_SIZE = 1024

SERIAL_NUMBER_FIELD_SIZE = 4
MAX_SERIAL_NUM = 10000


def special_sendto(socket_object, response, client_address):
    fail = random.randint(1, 3)
    if not (fail == 1):
        socket_object.sendto(response.encode(), client_address)
    else:
        print("Oops")


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    request_serial_number = 0
    ...

    ...

    if request_serial_number == MAX_SERIAL_NUM:
        request_serial_number = 0

    while True:
        message = input('Enter message to send: ')
        if message.lower() == 'exit':
            break
        serial_number_field = str(request_serial_number).zfill(SERIAL_NUMBER_FIELD_SIZE)
        special_sendto(sock, f'{serial_number_field}{message}'.encode(), (SERVER_IP, PORT))
        (response, remote_address) = sock.recvfrom(MAX_MSG_SIZE)

        request_serial_number += 1
