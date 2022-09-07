# Queue
class Queue:
    
    def __init__(self):
        self.queue = []
        self.MaxSize = 5

    def isEmpty(self):
        if len(self.queue)<1:
            return True
        else:
            return False

    def isFull(self):
        if len(self.queue)==self.MaxSize:
            return True
        else:
            return False

    def enqueue(self,item):
        if not(self.isFull()):
            self.queue.append(item)
        else:
            return None
    
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            self.queue.pop(0)
    
    def display(self):
        print(self.queue)

    # Front element of the queue.
    def peek(self):
        print(self.queue[0])

# Testing
queue = Queue()

queue.enqueue(4)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(7)
queue.dequeue()
queue.display()
queue.peek()





# queue = []

# def enqueue():
#     if len(queue)==n:
#         print("Queue is full.")
#     else:
#         e = int(input("Enter the element: "))
#         queue.append(e)
    
# def dequeue():
#     if len(queue)==0:
#         print("Queue is empty.")
#     else:
#         queue.pop(0)

# def display():
#     print(queue)

# n = int(input("Enter the size of queue: "))

# while True:
#     choice = int(input("Enter your choice: 1. add 2. remove 3. display 4. quit\n"))
#     if choice == 1:
#         enqueue()
#     elif choice == 2:
#         dequeue()
#     elif choice == 3:
#         display()
#     elif choice == 4:
#         break
#     else:
#         print("Enter the right choice: ")