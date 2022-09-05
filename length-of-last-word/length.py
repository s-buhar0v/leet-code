def length_of_last_word(s):
    splited = s.strip().split(' ')
    words = []

    for word in splited:
        if not word:
            continue

        words.append(word)

    return len(words[len(words) - 1])