#!/bin/python

"""
Problem Statement:
Given two integers, L and R, find the maximal value of A xor B, where A and B
satisfy the following condition:
L <= A <= B <= R

Input Format:
The input contains two lines; 
L is present in the first line and R in the second line

Constraints:
1 <= L <= R <= 10**3

Output Format:
The maximal value as mentioned in the problem statement.
"""

# Complete the function below.
def maxXor(l, r):
    # Set variables
    max_value = 0
    current_value = 0

    # Create list and index to use for iteration
    working_range = range(l, r + 1)
    wr_idx = range(len(working_range))

    # Iterate over the list to determine the max xor values for L and R
    for i in working_range:
        for j in wr_idx:
            current_value = i ^ working_range[j]
            if current_value > max_value:
                max_value = current_value
    return max_value

_l = int(raw_input())
_r = int(raw_input())

res = maxXor(_l, _r)
print res

