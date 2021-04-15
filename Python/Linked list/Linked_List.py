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
                print(n.data, "-->", end=" ")
                n = n.ref
            print("None")

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
        while n.ref != None:
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
            while(n.ref!=None):
                if n.ref.data==x:
                    break
                else:
                    n = n.ref
            if n.ref is None:
                print("Node is not present in the linked List.")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
    
    # Insert in the empty list
    def insert_empty(self,data):
        if self.head==None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty.")

    # Deleting from begining
    def delete_begin(self):
        if self.head==None:
            print("Linked list is already empty.")
        else:
            self.head = self.head.ref    

    # Delete from end
    def delete_end(self):
        n = self.head
        if n==None:
            print("Linked list is already empty.")
        elif n.ref==None:
            self.head=None
        else:
            while(n.ref!=None):
                if n.ref.ref==None:
                    break
                else:
                    n = n.ref
            n.ref = None
        
    # Delete in middle
    def delete_middle(self,x):
        n = self.head
        if n==None:
            print("Linked list is already emplty.")
        else:
            while(n.ref!=None):
                if (n.ref.data==x):
                    break
                else:
                    n = n.ref
            n.ref = n.ref.ref

               



# Printing
LL1 = LinkedList()
LL1.insert_empty(10)
LL1.add_begin(3)
LL1.add_end(1)
LL1.add_begin(5)
LL1.add_after(data=7, x=5)
LL1.add_before(data=80, x=7)
LL1.add_end(99) 
print("Before deleting...")
LL1.print_LL() # 5 80 7 3 10 1 99


print("\nAfter Deleting...")
LL1.delete_begin()
LL1.delete_middle(3)
LL1.delete_end()
LL1.print_LL() # 80 7 10 1 
