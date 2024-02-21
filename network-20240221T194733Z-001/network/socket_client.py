import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('127.0.0.1', 8222))
data = ''
while data != 'Bye':
    msg = input('Enter your message:\n')
    my_socket.send(msg.encode())
    data = my_socket.recv(1024).decode()
    print('the server sent ' + data)
print('closing client socket')
my_socket.close()
