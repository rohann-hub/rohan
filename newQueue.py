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
