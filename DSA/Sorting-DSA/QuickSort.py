# # Quick sorting using python.
# # So, here we create 2 functions, One for partition and another for sorting.


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quickSort(array, low, high):
    if low < high:
        part = partition(array, low, high)
        quickSort(array, low, part - 1)
        quickSort(array, part + 1, high)


data = [1, 7, 2, 10, -1, 9]
print("PREVIOUS ARRAY:", data)
size = len(data)
quickSort(data, 0, size - 1)
print("AFTER SORTING THIS ARRAY:", data)
