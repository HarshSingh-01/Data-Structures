from collections import deque

stack = deque()
# Psuhing elements
stack.append(1)
stack.append(12)
stack.append(34)
print("Stack After entering the elements:",stack)

#Poping elements
stack.pop()
stack.pop()
print("Stack after deleting elements:",stack)
