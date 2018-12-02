
# Double Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoubleList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.previous = None
            self.head = new_node
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.previous = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.previous = None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


myList = DoubleList
myList.prepend(1)

