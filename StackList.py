
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



##########################################

class Stack:
    def __init__(self, size):
        
        self.stack = []
        self.size = size
    
    def is_empty(self):
        
        return len(self.stack) == 0
    
    def is_full(self):
        
        return len(self.stack) == self.size
    
    def push(self, item):
      
        if self.is_full():
            print("Stack Overflow! Cannot push item.")
        else:
            self.stack.append(item)
            print(f"Item {item} pushed to stack.")
    
    def pop(self):
       
        if self.is_empty():
            print("Stack Underflow! Cannot pop item.")
        else:
            item = self.stack.pop()
            print(f"Item {item} popped from stack.")
            return item
    
    def peek(self):
        
        if self.is_empty():
            print("Stack is empty.")
        else:
            return self.stack[-1]
    
    def display(self):
        
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Current Stack:", self.stack)


stack = Stack(size=5)

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.pop()

stack.display()

stack.push(40)
stack.push(50)
stack.push(60) 
print("Top item is:", stack.peek())

print("Is stack empty?", stack.is_empty())  
print("Is stack full?", stack.is_full())  

     
