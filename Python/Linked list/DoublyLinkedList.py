# Doubly Linked List

class Node:
    def __init__(self,data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doublyLinkedList:
    def __init__(self,head=None):
        self.head = head

    def printLL(self):
        if self.head==None:
            print("Linked List is empty.")
        else:
            n = self.head
            while n!=None:
                print(n.data, end=" ")
                n = n.next

    def insertInEmptyList(self, data):
        if self.head==None:
            self.head = Node(data)

    def insertAtBegining(self, data):
        if self.head==None:
            self.insertInEmptyList(data)
        else:
            newNode = Node(data)
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def insertAtEnd(self, data):
        if self.head == None:
            self.insertInEmptyList(data)
        else:
            n = self.head
            while n.next!=None:
                n = n.next
            newNode = Node(data)
            newNode.prev = n
            newNode.next = None
            n.next = newNode

    def getNode(self, index):
        n = self.head
        if n==None:
            return None
        i = 0
        while(i<index and n!=None):
            n = n.next
            if n==None:
                break
            i += 1
        return n
    
    def insertAtPostion(self, index, data):
        if self.head==None or index==0:
            self.insertAtBegining(data)
        else:
            temp = self.getNode(index)
            if temp==None:
                self.insertAtEnd(data)
            else:
                newNode = Node(data)
                newNode.next = temp
                newNode.prev = temp.prev
                temp.prev.next = newNode
                temp.prev = newNode
        
    def deleteFromBeg(self):
        self.head = self.head.next
        self.head.prev = None


    def deleteFromEnd(self):
        if self.head.next==None:
            self.deleteFromBeg()
        else:
            n = self.head
            while n.next.next!=None:
                n = n.next
            n.next.prev = None
            n.next = n.next.next
    
    def deleteFromPosition(self, index):
        temp = self.getNode(index)
        if self.head.next == None or index==0:
            self.deleteFromBeg()
        elif temp==None or temp.next == None:
            self.deleteFromEnd()
        else:
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None
    
    def deleteWithData(self,data):
        temp = self.head
        while temp.next!=None:
            if temp.data==data:
                break
            temp = temp.next
        if temp.next==None:
            self.deleteFromEnd()
        elif temp.prev==None:
            self.head = temp.next
            temp.next.prev = None
        elif temp.next!=None:
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None
                
                          

# Testing
DLL = doublyLinkedList()

# Insertion
print("Insertion")

DLL.insertAtBegining(20)
DLL.insertAtBegining(40)
DLL.insertAtEnd(50)
DLL.insertAtEnd(48)
DLL.insertAtEnd(94)

DLL.insertAtPostion(5, 25)
DLL.printLL()

# Deletion
print("Deletion")

DLL.deleteFromBeg()
DLL.deleteFromEnd()
DLL.deleteFromPosition(6)
DLL.deleteWithData(25)

DLL.printLL()