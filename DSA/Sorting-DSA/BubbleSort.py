# Bubble sort in _Python

BubbleARR = [
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
for i in range(0, len(BubbleARR)):
    for j in range(0, len(BubbleARR) - i - 1):
        if BubbleARR[j] > BubbleARR[j + 1]:
            BubbleARR[j], BubbleARR[j + 1] = BubbleARR[j + 1], BubbleARR[j]

print(f"AFTER BUBBLE SORT:- {BubbleARR} Type OF : {type(BubbleARR)} ")
