from collections import deque

q = deque(maxlen=4)

# Left to right (FIFO)
q.appendleft(2)
q.appendleft(5)
q.appendleft(7)
print("Queue: ",q)

q.pop()
q.pop()
print("Queue: ",q)

# Right to left (FIFO)
q.append(2)
q.append(5)
q.append(7)
print("Queue: ",q)

q.popleft()
q.popleft()
print("Queue: ",q)