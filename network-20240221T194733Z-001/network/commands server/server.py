import socket
from random import randrange
from time import strftime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 1086))
server_socket.listen()
print('running')
(client_socket, client_address) = server_socket.accept()
client_socket.send(
        """Choose command: (enter num)
        1) Name
        2) Time
        3) Random
        
        "q" to quit""".encode()
)
data = ''
while True:
    data = client_socket.recv(1024).decode().lower()
    if data == 'q':
        client_socket.send('quitting'.encode())
        break
    elif data == '1':  # name
        print('client sent 1')
        client_socket.send('command INC'.encode())
    elif data == '2':  # time
        print('client sent 2')
        client_socket.send(strftime('%H:%M:%S').encode())
    elif data == '3':  # rand
        client_socket.send(str(randrange(1, 11)).encode())
    else:
        client_socket.send('unknown command'.encode())
client_socket.close()
server_socket.close()
