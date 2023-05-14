# Heap sort using _Python built in module -Heappush,-Heappop.

from _heapq import heappush, heappop


def heapfly(listOne):
    heap = []
    for a in listOne:
        heappush(heap, a)

    sort = []

    while heap:
        sort.append(heappop(heap))

    return sort


"""Call"""
listOne = [
    23,
    67,
    38,
    19,
    56,
    78,
    44,
    88,
    90,
    100,
    1200,
    346,
    789,
    845,
    4,
    6,
    1,
    3908,
    2,
    10,
]
hs = heapfly(listOne)
print(hs)
