import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8222))
server_socket.listen()
print('server is running')
(client_socket, client_address) = server_socket.accept()
print('client connected')

data = ''
while True:
    data = client_socket.recv(1024).decode()
    print('client sent: '+ data)
    if data.lower() == 'bye':
        data = ' '
    if data.lower() == 'quit':
        print('closing connection')
        client_socket.send('bye'.encode())
        break
    client_socket.send((data.upper() + '!!!').encode())
client_socket.close()
server_socket.close()