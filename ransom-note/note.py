# https://leetcode.com/problems/ransom-note/

from collections import Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    magazineLetters = Counter(magazine)
    ransomNoteLetters = Counter(ransom_note)

    for l in ransomNoteLetters:
        if l not in magazineLetters or ransomNoteLetters[l] > magazineLetters[l]:
            return False

    return True
