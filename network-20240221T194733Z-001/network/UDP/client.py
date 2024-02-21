import socket

SERVER_IP = '127.0.0.1'
PORT = 8821
MSG_MAX_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    while True:
        message = input('Enter message to send: ')
        if message.lower() == 'exit':
            break
        sock.sendto(message.encode(), (SERVER_IP, PORT))
        (bytes_response, remote_address) = sock.recvfrom(MSG_MAX_SIZE)
        data = bytes_response.decode()
        print('the server sent '+data)
    sock.sendto(b'exit', (SERVER_IP, PORT))
