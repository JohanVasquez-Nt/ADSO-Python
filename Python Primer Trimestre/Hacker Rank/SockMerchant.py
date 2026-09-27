#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    
    for z in range(n):
        for i in range(n-1):
            if ar[i] > ar[i+1]:
                ar[i] , ar[i+1] = ar[i+1] , ar[i]
                
    i = 0
    contador = 0
    
    while i < n - 1:
        if ar[i] == ar[i + 1]:
            contador += 1
            i += 2
        else:
            i += 1
                
    return contador       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
