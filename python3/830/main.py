"""
Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. 
For example, given [10, 7, 76, 415], you should return 77641510.
"""


import argparse


def cli_input():
    parser = argparse.ArgumentParser(description='Process some integers.')
    args = parser.parse_args()

    print(f"{args}")

    pass


if __name__ == "__main__":
    cli_input()
    pass
