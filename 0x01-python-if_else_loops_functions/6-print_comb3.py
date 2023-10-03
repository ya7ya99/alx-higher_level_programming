#!/usr/bin/python3
for i in range(10):
    for n in range(i + 1, 10):
        if i == 8 and n == 9:
            print("{:d}{:d}".format(i, n))
        else:
            print("{:d}{:d}, ".format(i, n), end="")
