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
import argparse


def find_concatenation(str_example: str, words: list):
    result = []
    permutations = ["".join(item) for item in itertools.permutations(words)]

    for item in permutations:
        result += [i for i in range(len(str_example)) if str_example.startswith(item, i)]
    
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Process find all starting indices of substrings.'
    )
    parser.add_argument('--string', type=str, required=True)
    parser.add_argument('--words', nargs='*', type=str, required=True, help="list of words words")
    args = parser.parse_args()

    print("Text: ", args.string)
    print("words: ", args.words)
    print(find_concatenation(args.string, args.words))
