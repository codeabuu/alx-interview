#!/usr/bin/env python3

def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
def verify(index):
    if index is not None:
        print('Target', index)
    else:
        print('NA')
nos = [1,2,3,4,5]
tar = linear_search(nos, 3)
verify(tar)

