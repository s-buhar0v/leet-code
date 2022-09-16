# https://leetcode.com/problems/longest-palindrome

from collections import Counter

def longest_palindrome(s: str) -> int:
    chars = Counter(s)

    result = 0
    odd = 0

    for v in chars.values():
        if v > 1:
            if v % 2 == 0:
                result += v
            else:
                result += v - 1
                odd += 1
        else:
            odd += 1

    if odd > 0:
        result += 1

    return result