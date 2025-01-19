class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def delete_node(self, node):
        if self.head is None or node is None:
            return
        if self.head == node:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        node = None

    def traverse_forward(self):
        temp = self.head
        while temp:
            print(f"{temp.data} <-> ", end=" ")
            temp = temp.next
        print("NULL")

    def traverse_backward(self):
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        while temp:
            print(f"{temp.data} < >", end=" ")
            temp = temp.prev
        print("Null")



x = DoublyLinkedList()
x.insert_at_beginning(10)
x.insert_at_beginning(20)
x.insert_at_end(30)
x.insert_at_end(50)
print("after treaverse forward:")

x.traverse_forward()
print("after treaverse backwaard:")
x.traverse_backward() 


node_to_delete = x.head.next
x.delete_node(node_to_delete)
print("after deleting the node:")
x.traverse_forward()
