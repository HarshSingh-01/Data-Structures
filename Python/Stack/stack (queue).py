import queue
stack = queue.LifoQueue(3) # Here you can set size of stack

# Pushing elements
stack.put(10)
stack.put(12)
stack.put(13)
print("Stack after pushing:", stack)

# Poping elements
stack.get()
stack.get()
stack.get()
# stack.get(timeout=1) # This will generate error