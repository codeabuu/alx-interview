#!/usr/bin/python3
'''a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.'''


def minOperations(n):
    '''create operations'''
    if n <= 1:
        return n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)
    return n
