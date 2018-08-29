class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next



l = LinkedList()
l.head = Node(1)
n2 = Node(2)
n3 = Node(3)
l.head.next = n2
n2.next = n3
l.list_print()

