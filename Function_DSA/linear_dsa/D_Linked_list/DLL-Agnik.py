class List:
    def __init__(self,n):
        self.data=n
        self.prev=None
        self.next=None
class DLinkedList:
    def __init__(self):
        self.head=None
        self.last=None
    def create(self,data):
        newNode=List(data)
        if self.head is None:
            self.head=newNode
            self.last=newNode
        else:
            newNode.prev=self.last
            self.last.next=newNode
            self.last=newNode
    def insert_at_front(self,n):
        newNode=List(n)
        if self.head==None:
            self.create(n)
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    def insert_at_last(self,n):
        self.create(n)
    def insert_at_pos(self,pos,n):
        newNode=List(n)
        pos-=1
        temp=self.head
        while pos>0:
            pos-=1
            temp=temp.next
        newNode.prev=temp.prev
        newNode.next=temp.prev.next
        temp.prev.next=newNode
        temp.prev=newNode
    def delete_from_front(self):
        self.head=self.head.next
        self.head.prev=None
    def delete_from_end(self):
        self.last.prev.next=None
        self.last=self.last.prev
    def delete_from_random_pos(self,pos):
        pos-=1
        temp=self.head
        while pos>0:
            pos-=1
            temp=temp.next
        temp.next.prev=temp.prev
        temp.prev.next=temp.next
    def printL(self):
        
        temp=self.head
        temp2=self.last
        print("USING NEXT:-")
        while temp is not None:
            print(temp.data)
            temp=temp.next
        print("USING PREV:-")
        while temp2 is not None:
            print(temp2.data)
            temp2=temp2.prev
l=DLinkedList()
l.create(10)
l.create(20)
l.create(30)
l.create(40)
l.create(50)
print("original linked:-")
l.printL()
l.insert_at_front(5)
print("after inserting at front ")
l.printL()
l.insert_at_pos(3,60)
print("after inserting at position")
l.printL()
l.insert_at_last(100)
print("after inserting at last")
l.printL()
l.delete_from_front()
print("after deleting from front")
l.printL()
l.delete_from_end()
print("after")
l.printL()
l.delete_from_random_pos(3)
l.printL()