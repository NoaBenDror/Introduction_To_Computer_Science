from largest_and_smallest import largest_and_smallest
PASS = "Function 4 passed the test for the input: "
FAIL = "Function 4 failed the test for the input: "


def does_max_min_func_work():
    """a function that tests whether the function 'largest_and_smallest'
     works, specifically on edge cases"""
    does_it_work = True
    if largest_and_smallest(1, 3, 3) != (3, 1):
        print(FAIL + '1,3,3')
        does_it_work = False
    else:
        print(PASS + '1,3,3')

    if largest_and_smallest(6, -6, -6) != (6, -6):
        print(FAIL + '6,-6,6')
        does_it_work = False
    else:
        print(PASS + '6,-6,6')

    if largest_and_smallest(0, 0, 0) != (0, 0):
        print(FAIL + '0,0,0')
        does_it_work = False
    else:
        print(PASS + '0,0,0')

    if largest_and_smallest(19.7, 17, 17.9) != (19.7, 17):
        print(FAIL + '19.7,17,17.9')
        does_it_work = False
    else:
        print(PASS + '19.7,17,17.9')

    if largest_and_smallest(17, 17.9, 19.7) != (19.7, 17):
        print(FAIL + '17,17.9,19.7')
        does_it_work = False
    else:
        print(PASS + '17,17.9,19.7')

    return does_it_work


if __name__ == '__main__':
    does_max_min_func_work()
