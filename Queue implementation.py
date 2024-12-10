## Queue implementation using linked list
class node:
    def __init__(self, data , next=None):
        self.data = data
        self.next = None
class queue:
    def __init__(self):
        self.front = None
        self.rare = None
    
    def enqueue(self , val):
        new_node = node(val)
        if self.rare is None:
            self.front = self.rare = new_node
        else:
            self.rare.next = new_node
            self.rare = new_node
        print(f"{val} is added to the Queue")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        dequeue_val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rare = None
        print(f"{dequeue_val} is removed from the Queue")
        return dequeue_val

    def is_empty(self):
        return  self.front is None
    
    def size(self):
        queue_size = 0
        current_node = self.front
        while current_node:
            queue_size +=1
            current_node = current_node.next
        return queue_size
    
    def front_element(self):
        if self.front is None:
            return None
        return self.front.data
    
    def display(self):
        if self.front is None:
            print("QUEUE IS EMPTY")
        else:
            current_node = self.front
            print("QUEUE ELEMENTS ARE: ")
            while current_node:
                print(f"## {current_node.data} ##")
                current_node = current_node.next
                if current_node:
                    print("--------->")

queue = queue()
while True:
    print("Enter any key\nA-Enqueue\nB-Dequque\nc-Display\nD-FRONT element\nE-SIZE of queue\nF-QUEUE IS EMPTY")
    choice = input("enter any key: ")
    if choice == 'A':
        print("ENQUE operation")
        val = int(input("Enter an element to push onto the stack: "))
        queue.enqueue(val)
    elif choice == 'B':
        print("DEQUEUE operation")
        queue.dequeue()
    elif choice == 'C': 
        print("DISPLAY operation")
        queue.display()
    elif choice == 'D':
        print("FRONT operation")
        front_value = queue.front_element()
        if front_value is None:
            print("Queue is empty")
        else:
            print(f"Top element of the stack: {front_value}")
    elif choice == 'E': 
        print("SIZE operation") 
        print(f"Queue size: {queue.size()}")
    elif choice == 'F':
        print("IS EMPTY OPERATION")
        if queue.is_empty:
            print("QUEUE is empty")
        else:
            print("QUEUE is full")
    else:
        print("Exit")
        break
