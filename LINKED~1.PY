class Node:
    def __init__(self,data=None):
        self.dato=0
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self, data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    
    def delete(self,index):
        currentNode=self.head
        for i in range(index-1):
            if(currentNode.next!=None):
                currentNode=currentNode.next
        currentNode.next=currentNode.next.next

    
myList=LinkedList()
for i in range(10):
    myList.add(i)





