import random
import socket
import chatlib  # To use chatlib functions or consts, use chatlib.****

SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5678


# HELPER SOCKET METHODS

def build_and_send_message(conn: socket.socket, cmd, data):
    """
    Builds a new message using chatlib, wanted code and message.
    Prints debug info, then sends it to the given socket.
    Parameters: conn (socket object), cmd (str), data (str)
    Returns: Nothing
    """
    message = chatlib.build_message(cmd, data)
    print(message)
    conn.send(message.encode())


# Implement Code


def recv_message_and_parse(conn: socket.socket):
    """
    Receives a new message from given socket,
    then parses the message using chatlib.
    Parameters: conn (socket object)
    Returns: cmd (str) and data (str) of the received message.
    If error occurred, will return None, None
    """
    try:
        full_msg = conn.recv(2048).decode()
        cmd, data = chatlib.parse_message(full_msg)
    except Exception as e:
        print(e)
        return None, None
    else:
        return cmd, data


def connect():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.connect((SERVER_IP, SERVER_PORT))

    return _socket


def error_and_exit(error_msg):
    print(error_msg)
    exit()


def login(conn):
    reply_cmd = ''
    while reply_cmd != chatlib.PROTOCOL_SERVER["login_ok_msg"]:
        username = input("Please enter username: \n")
        password = input("Please enter password: \n")
        data = '#'.join([username, password])
        build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["login_msg"], data)
        reply_cmd = recv_message_and_parse(conn)[0]
        if reply_cmd == chatlib.PROTOCOL_SERVER["login_ok_msg"]:
            print('Login Successful.')
            return
        elif reply_cmd == chatlib.PROTOCOL_SERVER["login_failed_msg"]:
            print('Login Failed.')


def logout(conn):
    build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["logout_msg"], '')


def build_send_recv_parse(conn, cmd, data):
    build_and_send_message(conn, cmd, data)
    msg_code, data = recv_message_and_parse(conn)
    return msg_code, data


def get_score(conn: socket.socket):
    highscore_table = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["highscore_msg"], '')[1]
    print(highscore_table)


def enum_question_choices(choices):
    """
    helper function. adds index of choice before the text

    param: list of the choices strings
    """
    index = 1
    new_list = []
    for choice in choices:
        new_list.append(f'{index}) {choice}')
        index += 1
    return '\n'.join(new_list)


def play_question(conn):
    try:
        cmd, data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["get_question"], '')
        if cmd != chatlib.PROTOCOL_SERVER["no_questions"]:
            data = str(data).split('#')
            question_id = data.pop(0)
            question = data.pop(0)
            choices = enum_question_choices(data)
            print(question)
            print(choices)
            choice = input('Answer: ')
            answer_cmd, answer_data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["send_answer"],
                                                            f'{question_id}#{choice}')
            if answer_cmd == chatlib.PROTOCOL_SERVER['correct_answer']:
                print(random.choice(['YES!', 'CORRECT', 'YES! GOOD ANSWER!']))
            elif answer_cmd == chatlib.PROTOCOL_SERVER['wrong_answer']:
                correct_answer = answer_data
                print(f'\nX Wrong answer X\nthe correct answer is #{correct_answer}\n')

        else:
            print('no questions left')
    except Exception as e:
        print(e)
        return


def get_logged_users(conn: socket.socket):
    users = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT['get_logged_users'], '')[1]
    print(users)


def main():
    sock = connect()
    login(sock)
    choice = ''
    while True:
        choice = input(
                """p        Play a question
s       Get my score
h       Get highscore table
l       Get logged users
q       Quit
Please enter your choice: """).lower()
        if choice == 's':
            print(build_send_recv_parse(sock, chatlib.PROTOCOL_CLIENT["my_score_msg"], '')[1])  # prints my_score
        elif choice == 'h':
            print(build_send_recv_parse(sock, chatlib.PROTOCOL_CLIENT["highscore_msg"], '')[1])  # prints my_score
        elif choice == 'p':
            play_question(sock)
        elif choice == 'l':
            get_logged_users(sock)
        elif choice == 'q':
            logout(sock)
            break
    sock.close()


if __name__ == '__main__':
    main()
