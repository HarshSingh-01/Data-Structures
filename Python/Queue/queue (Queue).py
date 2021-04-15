import queue

q = queue.Queue(maxsize=4)

# adding element
q.put(12)
q.put(34)
q.put(56)
q.put(35)

# deleting element
q.get()
q.get()
q.get()
q.get()
q.get(timeout=1)