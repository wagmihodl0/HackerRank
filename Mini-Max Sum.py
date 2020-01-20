#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    '''
    Given five positive integers, find the minimum and maximum values that can 
    be calculated by summing exactly four of the five integers. 
    Then print the respective minimum and maximum values as a single line of 
    two space-separated long integers.
    '''
    min = 0
    max = 0

    asc = sorted(arr)

    for i in range(4):
        min += asc[i]
    for i in range(4,0,-1):
        max += asc[i]


    print("{} {}".format(min, max))



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
