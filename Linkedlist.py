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
 
