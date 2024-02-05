def mergeSort(list):
    '''
    sort list in ascending order
    returns a new sorted list
    divide: find midpoint of the list and divide into sublist
    conquor: recursively sort the sublist created in prev step
    combine: merge the sorted sublist created in prev step
    '''
    if len(list) <= 1:
        return list
    left_half, right_half = split(list)
    left = mergeSort(left_half)
    right = mergeSort(right_half)

    return merge(left, right)

def split(list):
    '''
    divide unsorted list at midpoint into sublist
    Returns two sublist-left and right
    '''
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    '''
    merges two lists(arrays) sorting them in the process
    Returns new list
    '''
    l =[]
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i = i + 1
        else:
            l.append(right[j])
            j = j + 1

    while i < len(left):
        l.append(left[i])
        i = i + 1

    while j < len(right):
        l.append(right[j])
        j = j + 1
    return l
def verify(list):
    n=len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify(list[1:])

mylist = [54,62,23,73,31,44,66,77,88]
l = mergeSort(mylist)
print(verify(mylist))
print(l)
print(verify(l))
