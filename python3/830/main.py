"""
Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. 
For example, given [10, 7, 76, 415], you should return 77641510.
"""


import argparse


def first_number(element):
    text = str(element)
    return text[:1]

def largest_number():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', nargs='*', type=int)
    args = parser.parse_args()

    lst = args.integers
    lst.sort(key=first_number, reverse=True)

    return ''.join(str(item) for item in lst)
    

if __name__ == "__main__":
    print(largest_number())
