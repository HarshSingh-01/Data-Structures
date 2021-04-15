queue = []

def enqueue():
    if len(queue)==n:
        print("Queue is full.")
    else:
        e = int(input("Enter the element: "))
        queue.append(e)
    
def dequeue():
    if len(queue)==0:
        print("Queue is empty.")
    else:
        queue.pop(0)

def display():
    print(queue)

n = int(input("Enter the size of queue: "))

while True:
    choice = int(input("Enter your choice: 1. add 2. remove 3. display 4. quit\n"))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter the right choice: ")