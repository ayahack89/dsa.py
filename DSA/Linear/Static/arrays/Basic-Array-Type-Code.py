# Array Typecode
import array as myarray

"""Array Typecode be like:-
   1) 'i'-Integer Type[2]
   2) 'f'-Floting Type[4]
   3) 'd'-Floting Type[8]
   4) 'u'-Unicode Charecter Type[2]"""

a = myarray.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = myarray.array("u", ["a", "b", "c", "d"])
c = myarray.array("d", [1.2, 2.3, 3.4, 4.5, 5.6])
d = myarray.array("f", [67.98, 11.10])
print(f"My Array: {a}")
print(f"My Array: {b}")
print(f"My Array: {c}")
print(f"My Array: {d}")
print(f"Type Code:- {a.typecode}")
print(f"Type Code:- {b.typecode}")
print(f"Type Code:- {c.typecode}")
print(f"Type Code:- {d.typecode}")
