stack=[]
def push():
    if len(stack)==n:
        print("Stack is full.")
    else:
        e = int(input("Enter the element: "))
        stack.append(e)
        print(stack)

def pop():
    if not stack:
        print("Stack is empty.")
    else:
        e = stack.pop()
        print("The poped element is ", e)
        print(stack)
        
n = int(input("Enter the size: "))

while True:
    print("Enter your choice \n1. Push \n2. Pop \n3. quit ")
    choice = int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter the correct choice")
