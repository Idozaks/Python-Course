def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) == 1:
       if letter_guessed.isalpha():
            if not letter_guessed in old_letters_guessed:
                return True
    return False
    
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print('X,' + ' ->'.join(old_letters_guessed))
        return False

def show_hidden_word(secret_word, old_letters_guessed):
    result = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            result.append(letter)
        else:
            result.append('_')
    return ' '.join(result)

def check_win(secret_word, old_letters_guessed):
    win = True
    for letter in secret_word:
        if letter not in old_letters_guessed:
            win = False
    return win