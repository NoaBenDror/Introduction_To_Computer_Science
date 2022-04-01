import math
EMPTY = 0


def illegal_in_row(board, row, num):
    """a function that checks if a given number is in row"""
    if num in board[row]:
        return True
    return False


def illegal_in_col(board, col, num):
    """a function that checks if given number is in column"""
    for i in range(len(board)):  # traverse the column col
        if board[i][col] == num:
            return True
    return False


def illegal_in_square(board, sqrt_board_len, row, col, num):
    """a function that checks if given number is in its square"""
    corner_row = row - (row % sqrt_board_len) # index of top row in square
    corner_col = col - (col % sqrt_board_len) # index of left column in square
    # these next lines traverse the square and check if num is in it
    for i in range(sqrt_board_len):
        for j in range(sqrt_board_len):
            if board[i+corner_row][j+corner_col] == num:
                return True
    return False


def illegal_placement(board, row, col, num):
    """a function that gets board, row, column, and number, and returns
    whether it is illegal to place this number in board[row][col]"""
    return (illegal_in_row(board, row, num) or
            illegal_in_col(board, col, num) or
            illegal_in_square(board, int(math.sqrt(len(board))),
                              row, col, num))


def find_next_empty(board, row, col):
    """a function that finds next empty cell in board (traversing down and
    then to the right). if there is no empty cell, it will return the first
    cell outside the board, meaning board[0][len(board)].
    this will be taken care by the calling function"""
    while True:
        row += 1  # move down
        if row == len(board):  # if we are out of the board (down)
            row = 0  # go to next col
            col += 1
            if col == len(board):  # if we are out of the board (right)
                return row, col
        if board[row][col] == EMPTY:  # found real empty cell
            return row, col


def solve_sudoku_helper(board, row, col):
    """this function gets sudoku board, row index, col index, and solves the
    sudoku starting from board[row][col] """
    if col == len(board):  # we have passed the last column - solving finished
        return True
    for num in range(1, len(board)+1):  # iterates number from 1 to board
        #  length until found legal placement
        if illegal_placement(board, row, col, num):
            continue
        board[row][col] = num  # place the number
        next_empty_cell = find_next_empty(board, row, col)
        # check if we can fill up the remaining empty cells
        if solve_sudoku_helper(board, next_empty_cell[0], next_empty_cell[1]):
            return True
        board[row][col] = EMPTY  # if not, empty this cell
    return False  # no placement worked, give up


def solve_sudoku(board):
    """a function that solves a given sudoku if it is solvable (and returns
     True). if the sudoku is unsolvable the function will return False"""
    if board[0][0] == EMPTY:  # the top left cell is empty
        first_empty_cell = 0, 0
    else:
        # find first empty cell
        first_empty_cell = find_next_empty(board, 0, 0)
    return solve_sudoku_helper(board, first_empty_cell[0],
                               first_empty_cell[1])


def print_k_subsets(n, k):
    """a function that gets an int number n, and an int number k<=n,
    and prints all subsets of {0,...,n-1} of size exactly k, as lists"""
    if k <= n:  # make sure we can create subsets
        cur_set = [False] * n
        print_k_subsets_helper(cur_set, k, 0, 0)


def print_k_subsets_helper(cur_set, k, index, picked):
    """this function gets current set, wanted size of subsets, index,
    and a counter that checks how many indices we've chosen. the function
    creates all sets including the given index, and all sets excluding the
    given index, and prints all of them"""
    if k == picked:  # we picked out k items
        print_set(cur_set)  # print the subset
        return
    if index == len(cur_set):  # if we reached the end of the list, backtrack
        return
    # runs on all sets that include this index
    cur_set[index] = True
    print_k_subsets_helper(cur_set, k, index+1, picked+1)
    #  runs on all sets that do not include this index
    cur_set[index] = False
    print_k_subsets_helper(cur_set, k, index + 1, picked)


def print_set(cur_set):
    """this function gets a current set, and prints it as a list"""
    subset_lst = list()
    for i in range(len(cur_set)):  # traverse the current set
        if cur_set[i]:  # means set needs to include this index
            subset_lst.append(i)  # add it to list
    print(subset_lst)


def fill_k_subsets(n, k, lst):
    """a function that gets an int number n, and an int number k<=n,
    and prints all subsets of {0,...,n-1} of size exactly k, as lists"""
    if k <= n:  # make sure we can create subsets
        cur_set = [False] * n
        fill_k_subsets_helper(cur_set, k, 0, 0, lst)


def fill_k_subsets_helper(cur_set, k, index, picked, lst):
    """this function gets current set, wanted size of subsets, index,
    a counter that checks how many indices we've chosen, and a list.
    the function creates all sets including the given index, and all
    sets excluding the given index, and adds all sets to lst"""
    if k == picked:  # we picked out k items
        lst.append(fill_lst(cur_set))  # add subset list to list of subsets
        return
    if index == len(cur_set):
        return
    # runs on all sets that include this index
    cur_set[index] = True
    fill_k_subsets_helper(cur_set, k, index+1, picked+1, lst)
    #  runs on all sets that do not include this index
    cur_set[index] = False
    fill_k_subsets_helper(cur_set, k, index + 1, picked, lst)


def fill_lst(cur_set):
    """this function gets current set, and returns the set as a list"""
    subset_lst = list()
    for i in range(len(cur_set)):  # traverse the current set
        if cur_set[i]:  # means set needs to include this index
            subset_lst.append(i)  # add it to list
    return subset_lst


def return_k_subsets(n, k):
    """a function that gets an int number n, and an int number k<=n,
    and returns a list of all subsets of {0,...,n-1} of size  k"""
    if k <= n:
        return return_k_subsets_helper(n, k, 0)


def return_k_subsets_helper(n, k, index):
    """a function that gets an int number n, and an int number k<=n, and
     an index, and returns a list of all subsets of {index,...,n-1}
    of size k"""
    if k == 0:
        return [[]]  # one list with length of 0
    if index == n:
        return []    # done working on 0..n-1 (as index)
    # build lists with index (first without, length k-1, then insert index to
    # the beginning of each subset)
    lst_with = return_k_subsets_helper(n, k-1, index+1)
    for l in lst_with:
        l.insert(0, index)
    # build lists without index
    lst_without = return_k_subsets_helper(n, k, index+1)
    return lst_with + lst_without  # append the two lists and return
