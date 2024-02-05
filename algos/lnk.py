#!/usr/bin/python3
class Node:
    data=None
    next_node = None
    def __init__(self, data):
        self.data = data

class Lnk_list:
    def __init__(self):
        self.head = None 

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def insert(self, data, index):
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position = position - 1
            prev = current
            nexts = current.next_node

            prev.next_node = new
            new.nexts = nexts

    def remove(self, key):
        current = self.head
        prev = None
        found = False
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node
       return current
