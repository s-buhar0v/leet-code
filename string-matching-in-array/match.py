# https://leetcode.com/problems/string-matching-in-an-array/

from typing import List


def string_matching(words: List[str]) -> List[str]:
    result = []
    for i in range(len(words)):
        for j in range(0, len(words)):
            if i == j:
                continue

            if words[j] in words[i] and words[j] != words[i]:
                result.append(words[j])

    return result