def input_list():
    """a function that gets strings from user's input,
    until he inputs an empty string, and then returns
    a list of all the strings """
    list1 = list()
    user_input = input()  # the user inputs a string
    while user_input != "":
        list1.append(user_input)  # adding his input to the list
        user_input = input()
    return list1


def concat_list(str_list):
    """a function that gets a list of strings and returns concatenation
     of the list's elements as one string, with spaces between the elements"""
    st1 = ""
    if not str_list:  # if the list is empty
        return st1  # return an empty string
    for i in str_list:
        st1 = st1 + " " + i  # concatenation of the elements
    st1 = st1[1:]  # making sure there is no space in the beginning
    return st1


def maximum(num_list):
    """ a function that gets list of numbers and returns the maximal number"""
    if not num_list:  # if the list is empty
        return None
    max_num = num_list[0]
    for i in num_list:
        if max_num < i:
            max_num = i
    return max_num


def is_cyclic_from_index(lst1, lst2, shift_lst2):
    """a function that gets two lists, and shift, and checks whether the
    second list is cyclic shift of the first list, with this specific shift.
    assumptions: the lists have equal length, shift_lst2<length"""
    i1 = 0  # index in lst1
    i2 = shift_lst2  # (cyclic) index in lst2
    length = len(lst1)
    while i1 < length:  # traversing lst1
        if lst1[i1] != lst2[i2]:  # the elements don't have equal value
            return False
        i1 = i1 + 1
        i2 = (i2+1) % length  # next cyclic index
    return True


def cyclic(lst1, lst2):
    """a function that gets two lists of int type numbers,
     and returns whether one list is cyclic permutation of the other"""
    if len(lst1) != len(lst2):  # the length of the lists is not equal
        return False
    if len(lst1) == 0:
        return True
    for shift in range(len(lst1)):  # checking cyclic permutation,
        #  by specific shift
        if is_cyclic_from_index(lst1, lst2, shift):
            return True
    return False


def does_it_have_seven(number):
    """a function that gets an int type number and
     checks if it has the digit 7 in it"""
    num_as_st = str(number)  # converts the type int number to string
    for c in num_as_st:
        if c == "7":  # if the number does have the digit 7
            return True
    return False


def seven_boom(n):
    """a function that gets an int type number, and returns a list
     of the 'seven boom' game, according to the number"""
    lst = list()
    for i in range(1, n+1):
        if i % 7 == 0 or does_it_have_seven(i):  # the number is a boom
            lst.append("boom")  # add "boom" to the list,
            #  instead of the boom number
        else:
            lst.append(str(i))  # if it's not a boom,
            #  add the number to the list
    return lst


def histogram(n, num_list):
    """ a function that gets a list of int type numbers,
     and an int type number, and returns the relevant histogram"""
    histogram_list = list()
    for num_on_histo in range(n):  # num_on_histo is each
        #  positive number lower than n
        counter = 0  # counts how many times the number appeared on the list
        for i in num_list:  # checking every element on the list
            if i == num_on_histo:  # if the number did appear
                counter += 1
        histogram_list.append(counter)  # adding the counter to the list
    return histogram_list


def prime_factors(n):
    """a function that gets an int type number,
    and returns a list of its prime factors"""
    list_factors = list()
    divisor = 2  # potential divisor
    checked_num = n  #
    while checked_num > 1:  # will always get here at a certain point
        if checked_num % divisor == 0:  # divides by divisor
            list_factors.append(divisor)  # add to the list
            checked_num = checked_num / divisor
        else:  # can not divide by divisor (any more)
            divisor = divisor + 1  # add 1 to the divisor.
            #  if it is not prime, it will fail anyway
    return list_factors


def cartesian(lst1, lst2):
    """a function that gets 2 lists and returns their cartesian product"""
    cartesian_list = list()
    for i in lst1:
        for c in lst2:
            small_list = [i, c]  # matching the elements
            # according to cartesian rules, and then putting
            #  it in a list that its length is 2
            cartesian_list.append(small_list)  # adding the list above
            #  to a bigger list
    return cartesian_list


def pairs(num_list, n):
    """a function that gets a list of int type numbers,
    and an int type number, and returns a list of all the pairs on the list
    that their sum equals that number"""
    pairs_equal_n = list()
    for i in range(len(num_list)):  # a loop traversing the given list
        checked_index = i+1
        #  these next lines traverse the list from i+1
        #  and checks i with checked_index
        while checked_index < len(num_list):
            if num_list[i] + num_list[checked_index] == n:
                pairs_equal_n.append([num_list[i], num_list[checked_index]])
                break  # found a pair - no need to check the rest for this i
            checked_index += 1
    return pairs_equal_n
