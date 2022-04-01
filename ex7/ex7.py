def print_to_n(n):
    """a function that gets n (int number) and prints 1 to n numbers"""
    if n < 1:
        return
    else:
        (print_to_n(n-1))  # print all numbers before n
        print(n)  # print n


def print_reversed(n):
    """a function that gets n (int number) and prints n to 1 numbers"""
    if n < 1:
        return
    else:
        print(n)  # print n
        print_reversed(n-1)  # print all numbers before n


def is_prime(n):
    """a function that gets n (int number) and checks if it is prime"""
    if n <= 1:
        return False  # int smaller than 2 can't be prime (definition)
    return not has_divisor_smaller_than(n, n//2+1)  # a number has no divisor
    #  larger than half the number


def has_divisor_smaller_than(n, i):
    """a function that gets two int numbers, and checks if the first number
     has a divisor smaller than the second number"""
    if i == 2:
        return False  # since 1 is not considered as a divisor
    elif n % (i-1) == 0:  # has a divisor
            return True
    else:
        return has_divisor_smaller_than(n, i-1)


def exp_n_x(n, x):
    """a function that gets n-int number, and x-float number, and returns
    it's exponential sum"""
    if n == 0:
        return 1
    else:
        return power(x, n)/factorial(n) + exp_n_x(n-1, x)  # sum n and n-1


def factorial(n):
    """a function that gets a number and returns it's factorial"""
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)


def power(x, n):
    """a function that gets x- base, and n- exponent, and returns the
    exponentiation"""
    if n == 0:
        return 1
    else:
        return x*power(x, n-1)


def play_hanoi(hanoi, n, src, dest, temp):
    """a function that implements hanoi towers game"""
    if n <= 0:
        return
    else:
        play_hanoi(hanoi, n-1, src, temp, dest)  # move n-1 from src to temp
        hanoi.move(src, dest)  # move bottom ring from src to dest
        play_hanoi(hanoi, n-1, temp, dest, src)  # move back n-1 from temp to
        #  dest


def print_sequences(char_list, n):
    """a function that gets list of chars and n-int number, and prints all
     permutations of those chars in length n"""
    if n == 0:
        print("")  # sequence length 0 is actually an empty string
    else:
        string_list = build_sequences(char_list, n)  # build a list
        #  of possible sequences
        for s in string_list:
            print(s)  # print each possible sequence in the list


def build_sequences(char_list, n):
    """a function that gets list of chars, and n-int number, and returns
     an n length list of possible sequences"""
    if n == 1:  # sequence length is 1
        return char_list  # this is the list of possible sequences length 1
    else:
        # this next line builds list of possible sequences with n-1 length
        prev_string_list = build_sequences(char_list, n-1)
        result_string_list = list()
        for s in prev_string_list:
            for c in char_list:
                result_string_list.append(s + c)  # add each char to each
                #  element in possible sequences list
        return result_string_list


def print_no_repetition_sequences(char_list, n):
    """a function that gets list of chars and n-int number, and prints all
    permutations of those chars in length n without chars repetition on the
    same sequence """
    if n == 0:
        print("")  # sequence length 0 is actually an empty string
    else:
        # this next line builds a list of possible sequences
        string_list = build_no_repetition_sequences(char_list, n)
        for s in string_list:  # print each possible sequence in the list
            print(s)


def build_no_repetition_sequences(char_list, n):
    """a function that gets list of chars, and n-int number, and returns
    an n length list of possible sequences without chars repetition on
    the same sequence(assuming no repeated chars on char_list)"""
    if n == 1:  # sequence length is 1
        return char_list  # this is the list of possible sequences length 1
    else:
        # this next line builds list of possible sequences with n-1 length
        prev_string_list = build_no_repetition_sequences(char_list, n-1)
        result_string_list = list()
        for s in prev_string_list:
            for c in char_list:
                if c not in s:  # make sure we don't repeat the same char
                    result_string_list.append(s + c)  # add each char to each
                    #  element in possible sequences list
        return result_string_list


def parentheses(n):
    """ a function that gets n-int number, and returns a list with all n
    valid pairs of parentheses"""
    seq_lst = list()
    return parentheses_helper(0, 0, "", n, seq_lst)


def parentheses_helper(left, right, s, n, seq_lst):
    """a function that gets number of right parentheses, number of left
    parentheses, a string of parentheses, number of pairs of
    parentheses, and a list of parentheses permutations and returns
    a list of all possible sequences"""
    if right == n:  # completed a sequence
        seq_lst.append(s)
    elif left < n:
        # add left parentheses
        parentheses_helper(left + 1, right, s + "(", n, seq_lst)
    if right < left:
        # add right parentheses
        parentheses_helper(left, right + 1, s + ")", n, seq_lst)
    return seq_lst


def up_and_right(n, k):
    """a function that gets n- steps right, and k- steps up, and prints all
    paths from (0,0) to (n,k)"""
    up_and_right_helper(n, k, "")


def up_and_right_helper(n, k, path_str):
    """this function gets n,k (from up_and_right function) and a string that
    represents movement path, and prints all paths to (n,k)"""
    if n == 0 and k == 0:  # got to (0,0)
        print(path_str)
    if n > 0:
        up_and_right_helper(n - 1, k, path_str + "r")  # build paths to the
        #  position (n-1,k) and add to them "r"
    if k > 0:
        up_and_right_helper(n, k - 1, path_str + "u")  # build paths to the
        #  position (n,k-1) and add to them "u"


def flood_fill(image, start):
    """a function that gets two dimensional matrix and a tuple representing
    position in the matrix, and fills the matrix with "*" according to
    instructions """
    if image[start[0]][start[1]] == ".":  # the index we are looking at is "."
        image[start[0]][start[1]] = "*"  # change it to "*"
        flood_fill(image, (start[0]-1, start[1]))  # move up
        flood_fill(image, (start[0]+1, start[1]))  # move down
        flood_fill(image, (start[0], start[1]-1))  # move left
        flood_fill(image, (start[0], start[1]+1))  # move right