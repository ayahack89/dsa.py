# Create an instance of a specified class and display the namespace of the said instance.
class students:
    def __init__(self,stu_id,stu_name,stu_age):
        self.stu_id=stu_id
        self.stu_name=stu_name
        self.stu_age=stu_age
    
    def print(self):
        print(self.stu_id,self.stu_name,self.stu_age)
    
    def get_stu_id(self):
        return self.stu_id
    def get_stu_name(self):
        return self.stu_name
    def get_stu_age(self):
        return self.stu_age


stu_id=str(input("Enter your student ID: "))
stu_name=str(input("Enter your student name: "))
stu_age=int(input("Enter your age: "))

oop=students(stu_id,stu_name,stu_age)

x=oop.get_stu_id()
y=oop.get_stu_name()
z=oop.get_stu_age()
print(x)
print(y)
print(z)

    
        