# Protocol Constants

CMD_FIELD_LENGTH = 16  # Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4  # Exact length of length field (in bytes)
MAX_DATA_LENGTH = 10 ** LENGTH_FIELD_LENGTH - 1  # Max size of data field according to protocol
MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol
DATA_DELIMITER = "#"  # Delimiter in the data part of the message

# Protocol Messages 
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
    "login_msg" : "LOGIN",
    "logout_msg": "LOGOUT",
    "highscore_msg": "HIGHSCORE",
    "my_score_msg": "MY_SCORE",
    "get_question": "GET_QUESTION",
    "send_answer": "SEND_ANSWER",
    'get_logged_users': 'LOGGED'
}  # .. Add more commands if needed

PROTOCOL_SERVER = {
    "login_ok_msg"    : "LOGIN_OK",
    "login_failed_msg": "ERROR",
    "no_questions": "NO_QUESTIONS",
    'correct_answer': 'CORRECT_ANSWER',
    'wrong_answer': 'WRONG_ANSWER'
}
# Other constants

ERROR_RETURN = None


def build_message(cmd: str, data: str):
    """
    Gets command name (str) and data field (str) and creates a valid protocol message
    Returns: str, or None if error occured
    """
    if len(cmd) > CMD_FIELD_LENGTH or len(data) > MAX_DATA_LENGTH:
        return None
    command_str = cmd + ''.join([' '] * (CMD_FIELD_LENGTH - len(cmd)))
    full_msg = '|'.join([command_str, str(len(data)).zfill(4), data])
    return full_msg


def parse_message(data: str):
    """
    Parses protocol message and returns command name and data field
    Returns: cmd (str), data (str). If some error occured, returns None, None
    """
    if len(data) > MAX_MSG_LENGTH:
        return ERROR_RETURN, ERROR_RETURN
    try:
        if len(split_fields := data.split('|')) == 3:  # if there are 3 parts separated by |
            if len(split_fields[0]) == 16:  # if the command part's len is 16
                if len(split_fields[1]) == 4:  # if the len part is zfilled with 0's
                    if int(split_fields[1]) == len(split_fields[2]):
                        cmd = split_fields[0].strip()
                        msg = split_fields[2]
                        # The function should return 2 values
                        return cmd, msg
    except ValueError:
        pass
    return ERROR_RETURN, ERROR_RETURN


def split_data(msg: str, expected_fields):
    """
    Helper method. gets a string and number of expected fields in it. Splits the string
    using protocol's data field delimiter (|#) and validates that there are correct number of fields.
    Returns: list of fields if all ok. If some error occured, returns None
    """
    data = msg.split(DATA_DELIMITER)
    if len(data) == expected_fields + 1:
        return data
    else:
        return [ERROR_RETURN]


def join_data(msg_fields: list):
    """
    Helper method. Gets a list, joins all of it's fields to one string divided by the data delimiter.
    Returns: string that looks like cell1#cell2#cell3
    """
    return DATA_DELIMITER.join(msg_fields)
