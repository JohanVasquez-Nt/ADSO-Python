#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    t1 , t2 , t3 , t4 , t5 = 1, 2, 3, 4, 5
    c1 , c2 , c3 , c4 , c5 = 0, 0, 0, 0, 0
    for birds in arr:
        if birds == t1:
            c1 += 1
        elif birds == t2:
            c2 += 1
        elif birds == t3:
            c3 += 1
        elif birds == t4:
            c4 += 1
        elif birds == t5:
            c5 += 1
    if c1 >= c2 and c1 >= c3 and c1 >= c4 and c1 >= c5:
        return t1
    elif c2 >= c1 and c2 >= c3 and c2 >= c4 and c2 >= c5:
        return t2
    elif c3 >= c1 and c3 >= c2 and c3 >= c4 and c3 >= c5:
        return t3
    elif c4 >= c1 and c4 >= c2 and c4 >= c3 and c4 >= c5:
        return t4
    elif c5 >= c1 and c5 >= c2 and c5 >= c3 and c5 >= c4:
        return t5

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
