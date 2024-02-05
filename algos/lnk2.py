class Node:
    data = None
    nextNode = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class linkedList:
    head = None
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.nextNode
        return count

    def add(self, data):
        '''adds a new node with data at head of list
        this takes O(1)
        '''
        new_node = Node(data)
        new_node.nextNode = self.head
        self.head = new_node

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.nextNode
        return None
    def insert(self, data, index):
        if index == 0:
            self.add(data)
        elif index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = node.nextNode
                position = position - 1
            prev = current
            nexts = current.nextNode

            prev.nextNode = new
            new.nextNode = nexts

    def remove(self, key):
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.nextNode
            elif current.data == key:
                found =True
                previous.nextNode = current.nextNode
            else:
                prev = current
                current = current.nextNode
        return current

    def nodeatindex(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while postition < index:
                current = current.nextNode
                position += 1

            return current


    def __repr__(self):

        nodes =[]
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.nextNode is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.nextNode
        return '-> '.join(nodes)
