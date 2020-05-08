def has_negatives(a):

    """
    Returns which positive integers in the list have corresponding
    negative integers.
    """
    dict = {}
    matching_nums = []

    for x in a:
        x = abs(x)
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1

    for key, value in dict.items():
        if value > 1:
            matching_nums.append(key)
    return matching_nums

if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
