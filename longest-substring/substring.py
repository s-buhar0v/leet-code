def length_of_longest_substring(str):
    char_set = set()

    i = 0
    j = 0
    max_length = 0
    while i < len(str):
        while str[i] in char_set:
            char_set.remove(str[j])
            j += 1

        char_set.add(str[i])
        max_length = max(max_length, i - j + 1)

        i += 1

    return max_length
