# Basic Heap sort in _Python.


def heapsort(aR):
    n = len(aR)
    # Build Max Heap_
    for maxi in range(n // 2 - 1, -1, -1):
        heapsort(aR, n, maxi)

    # Extract element from heap one by one_
    for exe in range(n - 1, 0, -1):
        aR[exe], aR[0] = aR[0], aR[exe]  # Swap root and last element_
        heapsort(aR, exe, 0)

        return aR


def heapS(a, n, i):
    largest = i  # Initialize Largest Root_
    i = 2 * i + 1  # Left Child_
    r = 2 * i + 2  # Right Child_

    # Check if left child of root exist and is greter than root_
    if r < n and a[r] > a[largest]:
        largest = r

    # Change root , if needed
    if largest != i:
        a[i], a[largest] = a[largest], a[i]  # Swap
        heapS(a, n, largest)


"""Call"""
hola = heapS()
print(hola)
