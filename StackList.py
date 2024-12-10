
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        print(f"{val} is added to the stack")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None
        top_element = self.top
        self.top = top_element.next
        print(f"{top_element.data} is deleted from the stack")
        return top_element.data

    def size(self):
        stack_size = 0
        current_node = self.top
        while current_node:
            stack_size += 1
            current_node = current_node.next
        return stack_size

    def top_element(self):
        if self.top is None:
            return None
        return self.top.data

    def display(self):
        current_node = self.top
        print("Stack elements are:")
        while current_node:
            print(f'|| {current_node.data} ||')
            current_node = current_node.next
            print("------------>")

stack = Stack()
while True:
    print("Enter any key given below\nA-Push\nB-Pop\nC-Display\nD-Top\nE-SIZE\nEnter any other key for exit")
    choice = input("Enter any key: ")
    if choice == 'A':
        print("PUSH operation")
        val = int(input("Enter an element to push onto the stack: "))
        stack.push(val)
    elif choice == 'B':
        print("POP operation")
        stack.pop()
    elif choice == 'C': 
        print("DISPLAY operation")
        stack.display()
    elif choice == 'D':
        print("TOP operation")
        top_value = stack.top_element()
        if top_value is None:
            print("Stack is empty")
        else:
            print(f"Top element of the stack: {top_value}")
    elif choice == 'E': 
        print("SIZE operation") 
        print(f"Stack size: {stack.size()}")
    else:
        print("Exit")
        break
     
