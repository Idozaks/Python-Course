def print_hangman(num_of_tries):
    if num_of_tries <= 7:
        print(HANGMAN_PHOTOS[num_of_tries])

HANGMAN_PHOTOS = {1:"""    x-------x""", 2:"""    x-------x
    |
    |
    |
    |
    |""", 3:"""    x-------x
    |       |
    |       0
    |
    |
    |""", 4:"""    x-------x
    |       |
    |       0
    |       |
    |
    |""", 5:"""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 6:"""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 7:"""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}