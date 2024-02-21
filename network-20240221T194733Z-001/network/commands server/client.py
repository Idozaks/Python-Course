import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8222))
print(sock.recv(1024).decode())
data = ''
while data != 'quitting':
    choice = input()
    sock.send(choice.encode())
    data = sock.recv(1024).decode()
    print(data)
sock.close()
