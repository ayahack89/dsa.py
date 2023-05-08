# Selection Sorting
data = [7, 4, 9, 2, 6, 1, 5]
print(data)
print(type(data))
"""Outer loop"""
for a in range(0, len(data)):
    min_value = data[a]
    min_index = a
    """Inner loop"""
    for b in range(a + 1, len(data)):
        if min_value > data[b]:
            min_value = data[b]
            min_index = b
    temp = data[a]
    data[a] = data[min_index]
    data[min_index] = temp

    print("PROCESS-", data)


print("AFTER SORTING:-", data)
