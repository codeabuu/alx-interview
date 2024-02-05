#!/usr/bin/env python3

def binary_rec(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return binary_rec(list[midpoint + 1:], target)
            else:
                 return binary_rec(list[:midpoint], target)

def verify(index):
    if index is not None:
        print('Target: ', index)
    else:
        print('Not f')

numbers = [1,2,3,4,5,6]
result = binary_rec(numbers, 3)
verify(result)
