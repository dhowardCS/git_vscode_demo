import sys, math, os, datetime

sum = 0
for x in range(5, 11, 2):
    sum+=x
    print(sum)
else:
    print("Loop ended")

for i in range(2, 10, 2):
    for j in range(1, 9, 2):
        print(i, j)

else:
    print("Loop ended")
    