from lnk2 import linkedList

def merge(linkedList):
    '''
    sort linked list in ascending order
    recursively divide the linkedlist into sublists cotaining as single node
    repeatedly merge sublist to produce sorted sublist until one remains
    reutrn sorted list

    '''
    if linkedList.size() == 1:
        return linkedList
    elif linkedList.head is None:
        return linkedList

    left_half, right_half = split(linkedList)
    left = mergeSort(left_half)
    right - mergeSort(right_half)

    return merge(left, right)
def split(linkedList):
    '''
    divide unsorted lkn list
    '''
    if linkedList is None or linkedList.head is None:
        left_half = linkedList
        right_half = None

        return left_half, right_half
    else:
        size = linkedList.size()
        mid = size //2

        mid_node = linkedList.nodeatindex(mid - 1)

        left_half = linkedList
        right_half = linkedList()
        right_half.head = mid_node.nextNode
        mide_node.nextNode = None 

