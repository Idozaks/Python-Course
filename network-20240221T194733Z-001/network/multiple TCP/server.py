import socket, select

MAX_MSG_LENGTH = 1024
SERVER_IP = '0.0.0.0'
PORT = 5555


def main():
    print('setting up server...')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_IP, PORT))
        server_socket.listen()
        print('Listening for clients..')
        client_sockets = []
        while True:
            ready_to_read, ready_to_write, in_error = select.select([server_socket] + client_sockets, [], [])
            for current_socket in ready_to_read:
                current_socket: socket.socket  # type hinting
                if current_socket is server_socket:
                    (client_socket, client_address) = current_socket.accept()
                    print('New client joined!', client_address)
                    client_sockets.append(client_socket)
                else:
                    print('New data from client')


main()
