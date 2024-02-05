#!/usr/bin/env python3

def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        mid = (first + last) //2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return None

def verify(index):
    if index is not None:
        print('Target: ', index)
    else:
        print('NA')

nos = [1,2,3,4,5,6,7,8]
tar = binary_search(nos, 5)
verify(tar)
