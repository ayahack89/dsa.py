#ROW - COLUMN waise summation (include arrys)using nested loops.
#A) Row wise.
mine=[[11,-2,-3],
      [5,6,7],
      [8,9,10]]
counter=0
for a in mine:
    row=0
    for b in a:
        row+=b
    counter+=1
    print(f"The sum of the row {counter} is {row}")


print()


#B)Column wise.
lo=[[11,-2,-3],
      [5,6,7],
      [8,9,10]]
for c in range(3):
    sum=0
    for d in range(3):
        sum+=lo[d][c]
    print(f"The sum of the column {c+1} is {sum}")


