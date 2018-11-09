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
        print("Printing Linked List")
        head = self.head
        while head:
            print("->"+str(head.data),end="")
            head = head.next
        print("\n")
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
    # function to insert node at given position
    def add_node_position(self,data,position):
        node = Node(data)
        iterator = self.head
        counter = 2
        while counter < position:
            iterator = iterator.next
            counter += 1
        node.next = iterator.next
        iterator.next = node
    # function to access n'th element from end
    def get_node_from_end(self,n):
        if self.head is None:
            print("\nLinked List is empty")
            return
        else:
            first_iterator = self.head
            second_iterator = self.head
            # move second_iterator ahead by "n" nodes
            for i in range(n):
                second_iterator = second_iterator.next
            while second_iterator:
                first_iterator = first_iterator.next
                second_iterator = second_iterator.next
            print("Node at {}st position from end is {}".format(str(n),str(first_iterator.data)))
    # function to get the middle of linked list
    def get_middle_node(self):
        first_iterator = self.head
        second_iterator = self.head
        while second_iterator and second_iterator.next:
            first_iterator = first_iterator.next
            second_iterator = second_iterator.next.next
        print("Middle node is {}".format(str(first_iterator.data)))

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
    #linked_list.add_node_end(20)
    linked_list.print_linked_list()
    # insert node at position 4
    linked_list.add_node_position(10,4)
    linked_list.print_linked_list()
    # get 4th node from end
    linked_list.get_node_from_end(5)
    # get middle node for even nodes
    linked_list.print_linked_list()
    linked_list.get_middle_node()
    # get middle node for odd nodes
    linked_list.add_node_front(20)
    linked_list.print_linked_list()
    linked_list.get_middle_node()
