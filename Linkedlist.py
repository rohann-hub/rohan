class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        while temp and temp.next and temp.next.data != key:
            temp = temp.next
        if temp and temp.next:
            temp.next = temp.next.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

lst = LinkedList()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.insert(40)
lst.insert(50)

print("Linked list after insertion:")
lst.traverse()

lst.delete(20)
lst.delete(50)

print("\nLinked list after deletion:")
lst.traverse()




























## SinglyLInkedlist

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("EMPTY")
            return
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")  # To denote the end of the list

L = SingleLinkedList()
n1 = Node(10)
L.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4

L.display()
 
