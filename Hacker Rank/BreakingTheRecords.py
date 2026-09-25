#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    record_min = scores[0]
    record_max = scores[0]

    contador_min = 0
    contador_max = 0

    for i in range(n):
        if scores[i] < record_min:
            record_min = scores[i]
            contador_min += 1
        elif scores[i] > record_max:
            record_max = scores[i]
            contador_max += 1
    return (contador_max, contador_min)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
