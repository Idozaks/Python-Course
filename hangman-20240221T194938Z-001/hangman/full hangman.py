def choose_word(file_path, index):
    f = open(file_path, 'r')
    file_text = f.read()
    words = file_text.split(' ')
    f.close()
    word_list = list(dict.fromkeys(words))
    return len(word_list), words[index % len(words) - 1]
