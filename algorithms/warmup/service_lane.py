"""
For each input print the number that represents the largest vehicle type
that can pass through the service lane.
"""
# Get inputs N, T and WIDTHS from STDIN
N, T = map(int, raw_input().split())
WIDTHS = map(int, raw_input().split())

# service lane function
def service_lane(i, j):
    # set vehicle equal to the minimum vehichle width that can pass
    vehicle_type = min(WIDTHS[segment] for segment in range(i, j + 1))
    return vehicle_type

# print to STDOUT
while T > 0:
    # get i and j from STDIN
    i, j = map(int, raw_input().split())
    print service_lane(i, j)
    T -= 1

