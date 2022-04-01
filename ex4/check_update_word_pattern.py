from hangman import update_word_pattern

FAIL = "'update_word_pattern' function failed the test"
PASS = "'update_word_pattern' function passed the test"


def check_update_word_pattern():
    """a function that checks whether update_word_pattern function
     works for edge cases"""
    if update_word_pattern("chocolate", "ch_c_late", "o") != "chocolate":
        print(FAIL)
        return False
    if update_word_pattern("bottle", "bo__le", "t") != "bottle":
        print(FAIL)
        return False
    if update_word_pattern("extraordinary", "_____________", "x") !=\
            "_x___________":
        print(FAIL)
        return False
    if update_word_pattern("computer", "co_put__", "k") != "co_put__":
        print(FAIL)
        return False
    print(PASS)
    return True


if __name__ == '__main__':
    check_update_word_pattern()