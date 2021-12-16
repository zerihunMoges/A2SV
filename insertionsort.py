#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    i = n-1
    j = arr[n-1]
    strs = ''
    for i in range(n-1, -1, -1):
        if j < arr[i-1] and i != 0:
            arr[i] = arr[i-1]
            for i in range(len(arr)):
                strs += str(arr[i])+' '
            print(strs)
            strs = ''
            i-=1
        else:
            arr[i] = j
            for i in range(len(arr)):
                strs += str(arr[i])+' '
            print(strs)
            break

        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
