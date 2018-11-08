# create node class with "data" & "next"
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# create linked list class with "head"
class LinkedList:
    def __init__(self):
        self.head = None
    # function to print linked list
    def print_linked_list(self):
        head = self.head
        while head:
            print(str(head.data))
            head = head.next

# Code Execution starts here
if __name__ == '__main__':
    # Initialize empty linked list
    linked_list = LinkedList()
    # Create first node & add it to linked list
    linked_list.head = Node(1)
    # Create second and third node
    second = Node(2)
    third = Node(3)
    # Insert above two nodes to linked list
    linked_list.head.next = second
    second.next = third
    # print linked list
    linked_list.print_linked_list()
