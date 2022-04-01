def largest_and_smallest(num1, num2, num3):
    """a function that gets three numbers and returns
    the maximal number and the minimal number"""
    if num1 > num2:
        maximal = num1
        minimal = num2
    else:
        maximal = num2
        minimal = num1
    if num3 < minimal:
        minimal = num3
    elif num3 > maximal:
        maximal = num3

    return maximal, minimal





