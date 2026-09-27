#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    annio = f"12.09.{year}"
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return annio
    elif year % 4 == 0 and year < 1918:
        return annio
    elif year == 1918:
        annio = f"26.09.{year}"
        return annio
    else:
        annio = f"13.09.{year}"
        return annio

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
