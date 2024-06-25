"""
This problem was asked by Dropbox.

Given a string s and a list of words words, `
where each word is the same length, 
find all starting indices of substrings in s that is a 
concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], 
`return [0, 13], since "dogcat" starts at index 0 and "catdog" 
starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], 
return [] since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""

import itertools
import random


def find_concatenation(str_example: str, words: list):
    permutations = itertools.permutations(words)
    for item in permutations:
        print(list(item))
    
    pass


def generate_words(words: list, n: int = 100):
    return ''.join(random.choice(words) for _ in range(100))


if __name__ == "__main__":

    print(f"""find concatenation: {find_concatenation("barfoobazbitbyte", ["dog", "cat"])}""")
    pass
