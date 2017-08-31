"""
The Utopian tree goes through 2 cycles of growth every year. The first growth
cycle occurs during the monsoon, when it doubles in height. The second growth
cycle occurs during the summer, when its height increases by 1 meter.
Now, a new Utopian tree sapling is planted at the onset of the monsoon.
Its height is 1 meter. Can you find the height of the tree after N growth cycles?
"""
# function for utopian_growth
def utopian_growth(n):
    # set variables
    height = 1
    now = n - 1

    while now >= 0:
        # monsoon
        if (n - now) % 2 != 0:
            height *= 2
        # summer
        else:
            height += 1
        now -= 1
    return height

# number of test cases = 1st input from STDIN
T = int(raw_input())

# Get variables from STDIN
while T > 0:
    N = int(raw_input())
    # print results to STDOUT
    print utopian_growth(N)
    T -= 1
    
