# Creating a Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

# Linked List
class linkedList:
    def __init__(self):
        self.head = None

    def insertInEmptyList(self,data):
        if self.head==None:
            newNode = Node(data)
            self.head = newNode
        else:
            print("Linked List is not empty.")
    
    # Traversing
    def printLL(self):
        if self.head==None:
            print("Linked List is empty")
        else:
            n = self.head
            while n!=None:
                print(n.data, "-->", end=" ")
                n = n.next
            print("Null")

    # Insertion
    def insertAtBegining(self, data):
        if self.head==None:
            self.insertInEmptyList(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
    
    def insertAtEnd(self, data):
        if self.head==None:
            self.insertInEmptyList(data)
        else:
            newNode = Node(data)
            n = self.head
            while n.next!=None:
                n = n.next
            n.next = newNode
    
    def insertAfterNode(self, data, x):
        if self.head==None:
            self.insertInEmptyList(data)
        else:
            newNode = Node(data)
            n = self.head
            while n.next!=None:
                if n.data==x:
                    break
                else:
                    n = n.next
            if n is None:
                print("Node is not present in Linked List")
            else:
                newNode.next  = n.next
                n.next = newNode
        
    def insertBeforeNode(self, data, x):
        if self.head==None:
            self.insertInEmptyList(data)
        elif self.head.data==x:
            self.insertAtBegining(data)
        else:
            newNode = Node(data)
            n = self.head
            while n.next!= None:
                if n.next.data==x:
                    break
                else:
                    n = n.next
            if n is None:
                print("Node is not present in Linked List.")
            else:
                newNode.next = n.next
                n.next = newNode

    def IsLinkedListEmpty(self):
        if self.head==None:
            print("Linked List is already empty")
            return True
        else:
            print("Linked List is not empty")
            return False
    
    # Deletion
    def deleteAtBegining(self):
        if self.head==None:
            self.IsLinkedListEmpty()
        else:
            self.head = self.head.next
    
    def deleteAtEnd(self):
        if self.head==None:
            self.IsLinkedListEmpty()
        elif self.head.next==None:
            self.deleteAtBegining()
        else:
            n = self.head
            while n.next.next!=None:
                n = n.next
            n.next = n.next.next

    def deleteAtMiddle(self, x):
        if self.head==None:
            self.IsLinkedListEmpty()
        elif self.head.next==None:
            self.deleteAtBegining()
        else:
            n = self.head
            while n.next!=None:
                if n.next.data == x:
                    break
                else:
                    n = n.next
            if n.next is None:
                print("Element is not present")
            else:
                n.next = n.next.next

LL = linkedList()

# Insertion
print("Insertion")

LL.insertAtBegining(5)
LL.insertAtBegining(23)

LL.insertAtEnd(10)
LL.insertAtEnd(20)
LL.insertAfterNode(data=32, x=5)
LL.insertBeforeNode(data=40, x=20)
LL.printLL()

#Deletion
print("Deletion")
LL.deleteAtBegining()
LL.deleteAtEnd()
LL.deleteAtMiddle(32)
LL.printLL()

