from queue import PriorityQueue

q = PriorityQueue()

# Adding element
q.put(10)
q.put(30)
q.put(8)
q.put(50)
q.put(7)

# Deleting the prior element
q.get()
q.get()
q.get()