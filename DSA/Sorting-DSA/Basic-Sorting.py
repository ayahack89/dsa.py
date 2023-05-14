# Basic Sorting technique in array.
"""Here 'a' is an Array[list]."""
a = [23, 67, 38, 19, 56, 78, 44, 88, 90, 100, 1200, 346, 789, 845, 4, 6, 1, 3908, 2, 10]
print(a)
print(type(a))
for i in range(0, len(a)):
    for secondi in range(i + 1, len(a)):
        if a[i] > a[secondi]:
            temp = a[i]
            a[i] = a[secondi]
            a[secondi] = temp


print("-----------")
print("AFTER SORTING:-", a)
