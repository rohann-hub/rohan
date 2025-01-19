class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    
    def is_empty(self):
        return self.front is None

    
    def display(self):
        current = self.front
        while current:
            print(current.data, end="--->")
            current = current.next
        print("none")


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()  

print("remove element: ", q.dequeue())
print("remove element: ", q.dequeue())

    

q.display() 





























####### OR ##########
class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow! Cannot enqueue item.")
        else:
            self.queue.append(item)
            print(f"Item {item} enqueued to queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue item.")
        else:
            item = self.queue.pop(0)
            print(f"Item {item} dequeued from queue.")
            return item
        
    def front(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        else:
            return self.queue[0]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Current Queue:", self.queue)

queue = Queue(size=5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()

queue.dequeue()
queue.dequeue()

queue.display()

queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)

queue.display()

print("Front element:", queue.front())
print("Is queue empty?", queue.is_empty())
print("Is queue full?", queue.is_full())
