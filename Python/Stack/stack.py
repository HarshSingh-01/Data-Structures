# Stack

def create_stack():
    stack = []
    MaxSize = int(input("Max size of the stack: "))
    return (stack, MaxSize)

def isEmpty(stack):
    if len(stack)==0:
        return 1
    else: 
        return 0

def isFull(stack, MaxSize):
    if len(stack)==MaxSize:
        return 1
    else:
        return 0

def push(stack, MaxSize, item):
    if isFull(stack, MaxSize):
        print("Already Full")
        return -1
    else:
        stack.append(item)
        return 

def pop(stack):
    if isEmpty(stack):
        print("Already Empty")
    else:
        stack.pop()
        return

# Intializing Stack
stack, MaxSize = create_stack()

push(stack, MaxSize, 4)
print("Stack: ", stack)

push(stack, MaxSize, 7)
print("Stack: ", stack)

push(stack, MaxSize, 10)
print("Stack: ", stack)

pop(stack)
print("Stack: ", stack)

pop(stack)
print("Stack: ", stack)

push(stack, MaxSize, 20)
print("Stack: ", stack)




# stack=[]
# def push():
#     if len(stack)==n:
#         print("Stack is full.")
#     else:
#         e = int(input("Enter the element: "))
#         stack.append(e)
#         print(stack)

# def pop():
#     if not stack:
#         print("Stack is empty.")
#     else:
#         e = stack.pop()
#         print("The poped element is ", e)
#         print(stack)
        
# n = int(input("Enter the size: "))

# while True:
#     print("Enter your choice \n1. Push \n2. Pop \n3. quit ")
#     choice = int(input())
#     if choice==1:
#         push()
#     elif choice==2:
#         pop()
#     elif choice==3:
#         break
#     else:
#         print("Enter the correct choice")



