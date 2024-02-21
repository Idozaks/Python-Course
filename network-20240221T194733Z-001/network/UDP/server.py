import socket

SERVER_IP = '0.0.0.0'
PORT = 8821
MAX_MSG_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((SERVER_IP, PORT))
    print('server running')
    while True:
        (client_message, client_address) = server_socket.recvfrom(MAX_MSG_SIZE)
        data = client_message.decode()
        if data == 'exit':
            break
        print('client sent: ' + data)
        response = 'Hello ' + data
        server_socket.sendto(response.encode(), client_address)
    print('closing server')