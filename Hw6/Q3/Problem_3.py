


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node

    # Delete a node in a linked list
    def delete(self, data):
        if not self.head:
            return

        temp = self.head

        # Check if head node is to be deleted
        if self.head.data == data:
            head = temp.next
            print("Deleted node is " + str(self.head.data))
            return

        while temp.next:
            if temp.next.data == data:
                print("Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Node not found")
        return
    
### sort function starts from this line   
    def sort(self):
        l_size = self.size()
        current1 = self.head
        current2 = self.head.next
        for i in range(l_size):
            for j in range(l_size - i -1):
                if current1.data > current2.data:
                    temp = current1.data
                    current1.data = current2.data
                    current2.data = temp
                current2 = current2.next
            current1 = current1.next
            if current1 != None:
                current2 = current1.next




first_node = Node(11)

linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
first_node = Node(11)

print("The Linked List is:")
linked_list.print_list()

linked_list.sort()

print("After sorting, the Linked List is:")
linked_list.print_list()






