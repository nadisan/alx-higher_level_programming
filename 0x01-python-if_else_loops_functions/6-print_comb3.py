#!/usr/bin/python3
j = 89
for i in range(j):
    if (i / 10) >= (i % 10):
        continue
    else:
        print("{:02d}, ".format(i), end="")
print(89)
