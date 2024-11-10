def enqueue():
    n = int(input("Enter a element : "))
    queue.append(n)
    print()

def dequeue():
    if len(queue) == 0:
        print("QUEUE IS EMPTY")
        print("-------------------------")
    else:
        print(queue[0] , "is element deleted from the Queue")
        del queue[0]
        print()

def display():
    if len(queue) == 0:
        print("QUEUE IS EMPTY")
    else:
        print("ELEMENT OF THE QUEUE ARE : ")
        for ele in queue:
            print(ele, end=" ")
        print("\nFront ele of the queue : " , queue[0])
        print("RARE ele of the queue: ", queue[-1])
        print()

queue = list()
while(1):
    print("Enter any key\n1-insert\n2-delete\n3-Display\n4-Exit")
    option=int(input())
    if option == 1:
        print("insert the element")
        enqueue()
    elif option == 2:
        print("Delete the element")
        dequeue()
    elif option == 3:
        print("DISPLAY")
        display()
    else:
        print("EXIT")
        break
