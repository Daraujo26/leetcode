#
# Input is a sorted array, given a target, if the target is in the array return the index of the target.
# If not return None.

import math


def binarySearch(array, target):

    low = 0
    high = len(array)-1

    while low <= high:
        mid = math.floor((low + high).floor() / 2)
        guess = array[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

print(binarySearch([1, 3, 5, 7, 9], 3))