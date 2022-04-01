from ex3 import maximum


def test_maximum_func():
    """a function that tests whether the function 'maximum'
     works, specifically on edge cases"""
    did_it_pass = True
    if maximum([]) is not None:
        print("Failed test for empty list")
        did_it_pass = False
    else:
        print("Passed test for empty list")
    if maximum([0]) != 0:
        print("Failed test for list [0]")
        did_it_pass = False
    else:
        print("Passed test for list [0]")
    if maximum([5, 5, 5]) != 5:
        print("Failed test for list [5, 5, 5]")
        did_it_pass = False
    else:
        print("Passed test for list [5, 5, 5]")
    if maximum([7, 3, -15, 34, -25, 93]) != 93:
        print("Failed test for list [7, 3, -15, 34, -25, 93]")
        did_it_pass = False
    else:
        print("Passed test for list [7, 3, -15, 34, -25, 93]")
    return did_it_pass


if __name__ == '__main__':
    test_maximum_func()

