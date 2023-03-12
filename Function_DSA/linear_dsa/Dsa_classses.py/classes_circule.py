#Define class for circule:
#     data member - radius
#     methords - 1)defarea()
#                2)def.circumference()
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=(22/7)*((self.radius)**2)
        print(f"The area of the circle is {area}")
    def circumference(self):
        c=2*(22/7)*self.radius
        print(f"The circumference is {c}")
x=circle(int(input("Enter the radius: ")))
x.area()
x.circumference()
#due Analysis.
        