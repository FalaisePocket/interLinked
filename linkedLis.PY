class Node:
    def __init__(self,data=None):
        self.dato=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.arraylength=0
    ##O(1)
    def add(self, data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        self.arraylength+=1
    ##O(n)
    def delete(self,index):
        currentNode=self.head
        prev=currentNode
        if(currentNode!=None and index==0):
            self.head=currentNode.next
            del currentNode
            return
        for i in range(index):
            prev=currentNode
            currentNode=currentNode.next
        if currentNode==None:
            return
        prev.next=currentNode.next
        self.arraylength-=1
        del currentNode

    ##O(n)
    def insert(self, data, index):
        if(index==0):
            self.add(data)
            return
        ##Add Last(?
        if(index>self.length()):
            return
        currentNode=self.head
        prev=currentNode
        for i in range(index):
            prev=currentNode
            currentNode=currentNode.next
        newNode=Node(data)
        prev.next=newNode
        newNode.next=currentNode
        self.arraylength+=1

    def replace(self,data,index):
        currentNode=self.head
        for i in range(index):
            currentNode=currentNode.next
        currentNode.dato=data
        
    ##O(1)
    def length(self):
        return self.arraylength+0
    ##O(n)
    def get(self,index):
        currentNode=self.head
        for i in range(index):
            if(currentNode==None):
                return
            currentNode=currentNode.next
        return currentNode.dato
    #O(n)
    def fill(data,length):
        newList=LinkedList()
        for n in range(length):
            newList.add(data)
        return newList
    def arrayToLinkedList(array):
        newList=LinkedList()
        for n in array:
            newList.add(n)
        return newList


    

################################################################################

def merge(arr:LinkedList, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = LinkedList.fill(0,n1)
    R = LinkedList.fill(0,n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L.replace(arr.get(l+i),i)
 
    for j in range(0, n2):
        R.replace(arr.get(m + 1 + j),j)
 

    i = 0     
    j = 0    
    k = l    
 
    while i < n1 and j < n2:
        if L.get(i) <= R.get(j):
            arr.replace(L.get(i),k)
            i += 1
        else:
            arr.replace(R.get(j),k)
            j += 1
        k += 1
 

    while i < n1:
        arr.replace(L.get(i),k)
        i += 1
        k += 1

    while j < n2:
        arr.replace(R.get(j),k)
        j += 1
        k += 1
 
def mergeSort(arr:LinkedList, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

myList=LinkedList()
for i in range(10):
    myList.add(i)



'''for i in range(myList.length()):
    print(myList.get(i))

print("##################################################")
mergeSort(myList,0,myList.length()-1)

for i in range(myList.length()):
    print(myList.get(i))


'''
def greatnessToAnimals(animals)

def diseñarEspectaculo(n,m,k,animales,grandeza,apertura,*partes):




    return sortedAperture,sortedParts,stats



###se tienen n animales
###Se tiene m partes
###Se tiene K escenas
n=0
m=0
k=0

apertura=[]
parte1=[]
parte2=[]
