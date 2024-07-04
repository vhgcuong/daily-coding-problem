"""
This problem was asked by Google.

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""


if __name__ == "__main__":
    arr = [5, 1, 3, 5, 2, 3, 4, 1]
    subs = {}
    item = []
    for index, value in enumerate(arr):
        if value in item and len(item) > 0:
            subs[len(item)] = item
            item = []  
        item.append(value)

    if len(item) > 0: 
        subs[len(item)] = item

    max_key = max(subs.keys())
    print(subs[max_key])
