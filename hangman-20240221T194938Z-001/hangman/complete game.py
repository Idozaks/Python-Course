HANGMAN_PHOTOS = {1: """    x-------x""", 2: """    x-------x
    |
    |
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |
    |
    |""", 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}


def print_hangman(num_of_tries):
    """
    prints the current hangman stages
    """
    if num_of_tries <= 7:
        print(HANGMAN_PHOTOS[num_of_tries] + '\n')


def main():
    title_print()
    path = input('Enter path to word list file: ')
    index = input('Enter index to choose word from: ')
    word = choose_word(path, index)
    print(word)
    letters = []
    tries = 1
    print_hangman(tries)
    print(show_hidden_word(word, letters))
    while True:
        letter = input('Enter a letter: ')
        if not check_valid_input(letter, letters):
            if not letter.isalpha():
                print('X')
            else:
                print('X\n' + ' -> '.join(letters))
            continue
        if try_update_letter_guessed(letter, letters):
            if letter not in word:
                print(':(')
                tries += 1
                print_hangman(tries)
                print(show_hidden_word(word, letters))
            else:
                print(show_hidden_word(word, letters))
        if check_win(word, letters):
            print('WIN')
            break
        if tries == 7:
            print('LOSE')
            break


def title_print():
    HANGMAN_ASCII_ART = """
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
    MAX_TRIES = 6
    print('welcome to the game hangman')
    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)


def choose_word(file_path, index):
    """
    choose a word based on the index given

    :param file_path: path to word file
    :param index: index to choose the word
    :type file_path: str
    :type index: int
    :return: chosen word
    """
    index = int(index)
    f = open(file_path, 'r')
    file_text = f.read()
    words = file_text.split(' ')
    f.close()
    word_list = list(dict.fromkeys(words))
    return words[index % len(words) - 1]


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    validates the input string

    :param letter_guessed: string of the letter being guessed
    :type letter_guessed: str
    :param old_letters_guessed: list of letter already guessed
    :type old_letters_guessed: list
    :return: true if the input is valid
    """
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) == 1:
        if letter_guessed.isalpha() and letter_guessed not in old_letters_guessed:
            return True
    return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    tries to add the letter to the letters-guessed-list, based on its validity and
    whether it was already guess

    :param letter_guessed: letter being guessed
    :param old_letters_guessed: list of letters guessed
    :type old_letters_guessed: list
    :return: boolean based on the validity of the letter and whether it has been guessed
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print('X,' + ' ->'.join(old_letters_guessed))
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    returns a string that shows the letters guessed and the unguessed letters as _

    :param secret_word: the word
    :param old_letters_guessed: list of letters guessed
    """
    result = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            result.append(letter)
        else:
            result.append('_')
    return ' '.join(result)


def check_win(secret_word, old_letters_guessed):
    """
    checks win condition
    """
    win = True
    for letter in secret_word:
        if letter not in old_letters_guessed:
            win = False
    return win


if __name__ == '__main__':
    main()
