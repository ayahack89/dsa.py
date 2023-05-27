# Insertion sorting using python.
def insertionSort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >= key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [3, 5, 1, 8, 6, 2]
print("PREVIOUS LIST:- ", arr)
insertionSort(arr)
print(f"AFTER INSERTION SORTING:- {arr}")
