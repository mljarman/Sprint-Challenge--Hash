
from collections import Counter

def intersection(arrays):

    """
    Find the intersection between multiple lists of integers.
    """

    if arrays is None:
        print('Empty List')
    dict = {}
    intersects = []
    # create a dictionary with counts for each integer in the list of arrays:
    for x in arrays:
        for i in x:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
    # if the count of the array is higher than the number of arrays, must be
    # an intersection.
    for key, value in dict.items():
        if len(arrays) <= value:
            intersects.append(key)

    return intersects




if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(1000000,2000000)) + [1,2,3])
    # arrays.append(list(range(2000000,3000000)) + [1,2,3])
    # arrays.append(list(range(3000000,4000000)) + [1,2,3])

    arrays.append(list(range(1,5)) + [1,2,3])
    arrays.append(list(range(5,11)) + [1,2,3])
    arrays.append(list(range(11,16)) + [1,2,3])
    print(intersection(arrays))
