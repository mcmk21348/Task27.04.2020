#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    list_ = []
    open_list = ["[","{","("] 
    close_list = ["]","}",")"] 
    for i in s: 
        if i in open_list: 
            list_.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(list_) > 0) and
                (open_list[pos] == list_[len(list_)-1])): 
                list_.pop() 
            else: 
                return 'NO'
    if len(list_) == 0: 
        return 'YES'
    else: 
        return 'NO'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
