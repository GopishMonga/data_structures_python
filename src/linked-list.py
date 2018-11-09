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
        print("\nPrinting Linked List")
        head = self.head
        while head:
            print("->"+str(head.data),end="")
            head = head.next
        print()
    # function to insert node at front
    def add_node_front(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
    # function to insert node at end
    def add_node_end(self,data):
        node = Node(data)
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = node

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
    # insert node at front
    linked_list.add_node_front(4)
    linked_list.print_linked_list()
    # insert node at end
    linked_list.add_node_end(5)
    linked_list.print_linked_list()
