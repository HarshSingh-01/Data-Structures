# Circular Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circularLinkedList:

    def __init__(self):
        self.head = None 

    
    def circularListLength(self):
        currentNode =  self.head
        if currentNode == None:
            return 0
        count = 1
        while currentNode.next!=self.head:
            currentNode = currentNode.next
            count += 1
        return count
    
    def printLL(self):
        currentNode = self.head
        if currentNode == None:
            print("Linked List is empty.")
            return
        else:
            print(currentNode.data, end=" ")
            while (currentNode.next!=self.head):
                currentNode = currentNode.next
                print(currentNode.data, end =" ")
    
    def insertInEmptyList(self,data):
        newNode = Node(data)
        if self.head==None:
            self.head=newNode
            newNode.next = self.head
            
            
    def insertAtBeg(self, data):
        if self.head==None:
           self.insertInEmptyList(data)
           return
        else:
            newNode = Node(data)
            temp = self.head
            while temp.next!=self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head
            self.head = newNode

    def insertAtEnd(self, data):
        if self.head==None:
            self.insertInEmptyList(data)
            return
        else:
            newNode = Node(data)
            temp = self.head
            while temp.next!=self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head
    
    def getNode(self, index):
        currentNode = self.head
        if self.head==None:
            return None
        i = 0
        while i<index-1 and currentNode.next!=self.head:
            currentNode = currentNode.next
            i = i + 1
        return currentNode
    
    def insertAtPos(self,index, data):
        temp= self.getNode(index)
        if index==0:
            self.insertAtBeg(data)
            return
        elif temp==self.head or temp.next==self.head:
            self.insertAtEnd(data)
        else:
            newNode = Node(data)
            newNode.next = temp.next
            temp.next = newNode

    def deleteFromBeg(self):
        if(self.head==None):
            print("Linked List is empty.")
        temp = self.head
        while temp.next!=self.head:
            temp = temp.next
        self.head = self.head.next
        temp.next = self.head
    
    def deleteFromEnd(self):
        if(self.head==None):
            print("Linked List is empty.")
            return
        elif(self.head.next==self.head):
            self.deleteFromBeg()
            return
        else:
            temp = self.head
            while temp.next.next!=self.head:
                temp = temp.next
            temp.next = self.head

    def deleteFromPos(self, index):
        if (self.head==None):
            print("Linked List is empty.")
        elif(index==0):
            self.deleteFromBeg()
        else:
            temp = self.getNode(index)
            if temp.next==self.head:
                self.deleteFromEnd()
            else:
                temp.next = temp.next.next


# Testing
CLL = circularLinkedList()

#Insertion

CLL.insertAtBeg(23)
CLL.insertAtBeg(43)
CLL.insertAtBeg(31)
CLL.insertAtEnd(39)
CLL.insertAtEnd(98)
CLL.insertAtPos(3, 16)

CLL.printLL()

# Deletion 

CLL.deleteFromBeg()
CLL.deleteFromEnd()
CLL.deleteFromPos(5)
CLL.printLL()

