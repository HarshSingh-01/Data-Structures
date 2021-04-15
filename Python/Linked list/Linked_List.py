class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head=None
    
    # Traversing a Linked List
    def print_LL(self):
        if self.head==None:
            print("Linked List is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    # Adding at the begining
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    # Adding at the end
    def add_end(self,data):
        new_node = Node(data)
        # If linked list is empty
        if self.head==None:
            new_node = self.head
            self.head = new_node
        else:
            n = self.head
            while n.ref != None:
                n = n.ref
            n.ref = new_node
            new_node.ref = None

    # Adding after the element
    def add_after(self, data, x):
        n = self.head
        while n != None:
            if n.data == x:
                break
            else:
                n = n.ref
        if n is None:
            print("Node is not present in the Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # Adding before the element
    def add_before(self, data, x):
        if self.head==None:
            print("Link list is empty")
        elif self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            while(n!=None):
                if n.ref.data==x:
                    break
                else:
                    n = n.ref
            if n is None:
                print("Node is not present in the linked List.")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

                

               



# Printing
LL1 = LinkedList()
LL1.add_begin(3)
LL1.add_end(1)
LL1.add_begin(5)
LL1.add_after(data=7, x=5)
LL1.add_before(data=80, x=7)
LL1.add_end(99) 
LL1.print_LL() # 5 80 7 3 1 99