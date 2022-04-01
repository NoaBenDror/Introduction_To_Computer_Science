from wordsearch import does_len_match_index

FAIL = "test function 'does_len_match_index' failed"
PASS = "test function 'does_len_match_index' passed"
SEARCH_DIRECTIONS = 'udrlwxyz'


def check_wordsearch():
    """a function that checks 'does_len_match_index' function"""
    if not does_len_match_index(1, 1, 1, 0, 0, "u"):
        print(FAIL)
        return False
    if does_len_match_index(5, 1, 1, 0, 0, "u"):
        print(FAIL)
        return False
    if not does_len_match_index(7, 6, 9, 1, 2, "r"):
        print(FAIL)
        return False
    for direction in SEARCH_DIRECTIONS:
        if not does_len_match_index(3, 5, 5, 2, 2, direction):
            print(FAIL)
            return False
    for direction in SEARCH_DIRECTIONS:
        if does_len_match_index(4, 5, 5, 2, 2, direction):
            print(FAIL)
            return False
    print(PASS)
    return True


if __name__ == '__main__':
    check_wordsearch()