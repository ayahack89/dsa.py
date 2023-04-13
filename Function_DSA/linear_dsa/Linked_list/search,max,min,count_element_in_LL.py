#Create a LL in python & define 4 function - COUNT , MAX , MIN, SEARCH.
class List:
    def __init__(self,data):
        self.data=data
        self.address=None
class Linked_List:
    def __init__(self):
        self.head=None
        self.last=None
    def create(self,data):
        newNode=List(data)
        if self.head is None:
            self.head=newNode
            self.last=newNode
        else:
            self.last.address=newNode
            self.last=newNode
    def search_el(self,search):
        position=1
        found=False
        tempv=self.head
        while found is False and tempv is not None:
            if tempv.data==search:
                found=True
            else:
                tempv=tempv.address
                position=position+1
        if found==True:
            print(f"{search} element found at {position} !!")
        else:
            print("ERROR!!!!")
    def count_el(self):
        count=0
        temp=self.head
        while temp is not None:
            count=count+1
            temp=temp.address
        print(f"LL value Count ~ {count}")
    def maxvalue(self):
        temp=self.head
                

            
    def printList(self):
        temp=self.head
        while temp != None:
            print(temp.data)
            temp=temp.address


#CALL;
g=Linked_List()
a=int(input("Number of Inputs:- "))
for pk in range(0,a):
    g.create(int(input("NODE.DATA:: ")))
search=int(input("Enter a element to search: "))
g.search_el(search)
print("Count List-")
g.count_el()
print("Linked List")
g.printList()
print("END")
