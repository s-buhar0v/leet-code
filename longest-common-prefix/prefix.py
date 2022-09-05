def longest_common_prefix(strs):
    common_prefix = ''

    for index, value in enumerate(strs[0]):
        for str in strs:
            if index == len(str) or str[index] != value:
                return common_prefix

        common_prefix += value

    return common_prefix
