import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('127.0.0.1', 8222))
data = ''
while data.lower() != 'bye':
    msg = input('Enter message\n')
    my_socket.send(msg.encode())
    data = my_socket.recv(1024).decode()
    print('server sent: ' + data)
print('closing connection')
my_socket.close()
