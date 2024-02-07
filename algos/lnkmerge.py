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
    right = mergeSort(right_half)

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
        mid_node.nextNode = None 

        return left_half, right_half

def merge(left, right):
    '''merges 2 linked lst sorting by data in nodes
    returns a new merged list
    '''
    #create new linked list that contain nodes from
    #merging left and right

    merged = linkedList()

    merged.add(0)
    #set current to head of linked list
    current = merged.head

    #obtain head nodes for left and right linked list
    left_head = left.head
    right_head = right.head

    #iterate over left and right until we reach the tail node of either

    while left_head or right_head:
        if left_head is None:
            current.nextNode = right_head
            right_head = right_head.nextNode
        elif right_head is None:
            current.nextNode = left_head
            left_head = left_head.nextNode
        else:
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.nextNode = left_head
                left_head = left_head.nextNode
            else:
                current.nextNode = right_head
                right_head = right_head.nextNode
         current = current.nextNode

    head = merged.head.nextNode
    merged.head = head
    return merged


