#DLL 
#Double linked list all in one.....
class List:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class D_linked_L:
    def __init__(self):
        self.head = None
    def create(self,data):
        newNode=List(data)
        if self.head is None:
            self.head=newNode
            self.last=newNode
        else:
            newNode.previous=self.last
            self.last.next=newNode
            self.last=newNode
    def insert_at_front_position(self,data):
        newNode=List(data)
        newNode.next=self.head
        self.head=newNode
    def insert_at_random_position(self,data,position):
        temp=self.head
        newNode=List(data)
        position=position-1
        while(position>0):
            position=position-1
            temp=temp.next
        newNode.previous=temp.previous
        newNode.next=temp
        temp.previous.next=newNode
        temp.previous=newNode
    def insert_at_last_position(self,data):
        newNode=List(data)
        newNode.previous=self.last
        self.last.next=newNode
        self.last=newNode
    def delete_at_front(self):
        if self.head is None:
            print("Linked List is empty, can't delete.")
            return("ERROR")
        else:
            self.head=self.head.next
            self.head.previous=None
    def delete_at_random_position(self,position):
        delete_node=self.head
        position=position-1
        while(position>0):
            position=position-1
            delete_node=delete_node.next
        delete_node.previous=None
        delete_node=self.head.next
    def delete_at_last(self):
        if self.last is None:
            print("D Linked List is empty, can't delete.")
            return print("ERROR")
        else:
            self.last.previous=None
            self.last=self.last.next
    def printList(self):
        temp1=self.head
        temp2=self.last
        print("USING NEXT > ")
        while temp1 is not None:
            print(temp1.data)
            temp1=temp1.next
        print("USING PREVIOUS > ")
        while temp2 is not None:
            print(temp2.data)
            temp2=temp2.previous



#Call.........
p=D_linked_L()
while True:
    choice=str(input(" 1-CREATE NODES \n 2-PRINT ALL \n 3-INSERT AT FRONT POSITIONE \n 4-INSERT AT RANDOM POSITION \n 5-INSERT AT LAST POSITION \n 6-DELETE AT FRONT POSITION \n 7-DELETE AT RANDOM POSITION \n 8-DELETE AT LAST POSITION \n 9-END \n ENTER YOUR CHOICE:  "))
    if choice=='1':
        print("CREATE NODES;")
        a=int(input("Number of Inputs:- "))
        for j in range(0,a):
            p.create(int(input("Node.Data > ")))
    elif choice=='2':
        print("PRINT ALL;")
        print("Print all data....")
        p.printList()
        print("END")
    elif choice=='3':
        print("INSERT AT FIRST POSITION;")
        data=int(input("Enter a data to insert: "))
        p.insert_at_front_position(data)
        print("Data Inserted.")
        p.printList()
        print("END")
    elif choice=='4':
        print("INSERT AT RANDOM POSITION;")
        data=int(input("Insert a data to insert a random position: "))
        position=int(input("Enter a position to insert the given node: "))
        p.insert_at_random_position(data,position)
        print("Data Inserted.")
        p.printList()
        print("END")
    elif choice=='5':
        print("INSERT AT LAST POSITION;")
        data=int(input("Enter a data to insert at last position:  "))
        p.insert_at_last_position(data)
        print("Data Inserted.")
        p.printList()
        print("END")
    elif choice=='6':
        print("DELETE AT FRONT POSITION;")
        p.delete_at_front()
        print("Data Deleted.")
        p.printList()
        print("END")
    elif choice=='7':
        print("DELETE AT RANDOM POSITION;")
        position=int(input("Enter a position to delete the given node"))
        p.delete_at_random_position(position)
        print("Data Deleted.")
        p.printList()
        print("END")
    elif choice=='8':
        print("DELETE AT LAST POSITION;")
        p.delete_at_last()
        print("Data Deleted.")
        p.printList()
        print("END")
    elif choice=='9':
        break
    else:
        print("ERROR")
     