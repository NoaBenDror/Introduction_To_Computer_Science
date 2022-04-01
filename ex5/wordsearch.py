import sys
import os
SEARCH_DIRECTIONS = 'udrlwxyz'
NUM_INVALID = "Num of arguments invalid"
WORDS_INVALID = "Words file does not exist"
MATRIX_INVALID = "Matrix file does not exist"
SEARCH_INVALID = "Search direction invalid"
# this dictionary defines the movement from an index to the next
#  index according to the direction
DIRECTION_TO_MOVEMENT = {"u": (-1, 0),   # one row up
                         "d": (1, 0),    # one row down
                         "r": (0, 1),    # one column right
                         "l": (0, -1),   # one column left
                         "w": (-1, 1),   # one row down, one column right
                         "x": (-1, -1),  # one row up, one column left
                         "y": (1, 1),    # one row down, one column right
                         "z": (1, -1)}   # one row down, one column left


def check_input_args(args):
    """a function that gets a list of arguments and
     checks whether they are valid"""
    if len(args) != 5:
        return NUM_INVALID
    if not os.path.isfile(args[1]):
        return WORDS_INVALID
    if not os.path.isfile(args[2]):
        return MATRIX_INVALID
    for i in range(len(args[4])):
        if args[4][i] not in SEARCH_DIRECTIONS:
            return SEARCH_INVALID
    return None


def read_wordlist_file(filename):
    """a function that gets the name of the list of words file (assuming it
    exists), reads the words, and returns a list of these words"""
    f = open(filename)
    words_list = f.read().splitlines()
    f.close()
    return words_list


def read_matrix_file(filename):
    """ a function that gets the name of the matrix file(assuming it exists),
    reads the matrix, and returns a two-dimensional list of the letters
    in the matrix"""
    f = open(filename)
    matrix = list()
    while True:  # assuming valid input
        line = f.readline()  # read one line (as string) of the matrix
        if not line:  # reaches the last empty line
            break
        line_lst = line.split(',')  # creates list, removing ','
        line_lst[-1] = line_lst[-1][0]  # remove \n from last
        #  char in list(line)
        matrix.append(line_lst)  # add the line to the matrix
    f.close()
    return matrix


def does_len_match_index(word_len, num_rows, num_cols, row, col, direction):
    """a function that checks if match is possible considering the word's
    length only. if it's outside the matrix - the word would surely
    not match """
    # these two next lines calculate the row and column of last letter,
    #  by using the initial row and column, the direction movement,
    #  and the length
    last_letter_row = row + DIRECTION_TO_MOVEMENT[direction][0]*(word_len-1)
    last_letter_col = col + DIRECTION_TO_MOVEMENT[direction][1]*(word_len-1)
    if last_letter_row >= num_rows or last_letter_row < 0:
        return False
    if last_letter_col >= num_cols or last_letter_col < 0:
        return False
    return True


def does_word_match_index(word, matrix, row, col, direction):
    """a function that gets a word, matrix of letters, row index, column index
    and a search direction, and checks whether the word matches that
    index in the matrix"""
    #  this next line makes sure we are not outside the matrix
    if not does_len_match_index(len(word), len(matrix), len(matrix[0]), row,
                                col, direction):
        return False
    for letter in word:
        if letter != matrix[row][col]:  # word doesn't match
            return False
        # these two next lines move index in the matrix to the next position,
        #  according to direction
        row = row + DIRECTION_TO_MOVEMENT[direction][0]
        col = col + DIRECTION_TO_MOVEMENT[direction][1]
    return True


def update_dict_with_word(word, word_to_occurrences):
    """a function that gets a word and a current dictionary of word
    to occurrences, and adds the word to the dictionary if it does
    not exist, or adds 1 to the occurrences if it exists"""
    if word not in word_to_occurrences:
        word_to_occurrences[word] = 1
    else:
        word_to_occurrences[word] += 1
    return True  # we don't actually need to return value


def build_letter_to_indices(matrix):
    """a function that gets matrix of letters and returns a dictionary:
     key = letter, value = list of row,column in which the letter appears"""
    letter_to_indices = {}
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            letter = matrix[row][col]
            if letter not in letter_to_indices:
                # add the letter to the dictionary, with empty list
                letter_to_indices[letter] = []
            # add the index to the letter's list
            letter_to_indices[letter].append((row, col))
    return letter_to_indices


def find_words_in_matrix(word_list, matrix, directions):
    """a function that gets list of words, letters matrix,
    and string of search direction/s, and returns list of tuple that contains
    each word that appeared in the matrix, and how many times it appeared"""
    word_to_occurrences = {}
    letter_to_indices = build_letter_to_indices(matrix)
    # traverse the words, the first letter indices, and directions,
    #  and check match
    for word in word_list:
        if word[0] not in letter_to_indices:  # if first letter not in matrix,
            #  no need to check the word
            continue
        indices = letter_to_indices[word[0]]  # list of all the positions
        #  of the letter in the matrix (first letter in word)
        for pos in indices:
            for direction in directions:
                if does_word_match_index(word, matrix, pos[0], pos[1],
                                         direction):
                    update_dict_with_word(word, word_to_occurrences)
    return list(word_to_occurrences.items())  # convert dictionary
    #  to list


def write_output_file(results, output_filename):
    """a function that gets list of the results of the word search, and name
    of output file, and creates the output file which
    will contain that list"""
    f = open(output_filename, 'w')
    if results:
        for pair in results[:-1]:
            f.write(pair[0] + "," + str(pair[1]) + "\n")
        f.write(results[-1][0] + "," + str(results[-1][1]))  # no empty line
        # in the end
    f.close()


def filter_directions(directions):
    """a function that gets string of letters that represent
    the search directions, checks if some letters appear more than once,
    and returns filtered string, so that each letter will appear only once"""
    unique_directions = ""
    for char in directions:
        if char not in unique_directions:
            unique_directions = unique_directions + char
    return unique_directions


def process_word_search_in_matrix(args):
    """a function that gets a list of strings: list of words file name,
     matrix of letters file name, search directions, and an output file name.
    the function will validate the input, if valid- search the words in the
    matrix in the specified directions, and will write the results into
    the output file"""
    if check_input_args(args) is not None:
        print("Error: " + check_input_args(args))  # informative message
        #  about invalidity
    else:  # valid input
        list_of_words = read_wordlist_file(args[1])
        matrix = read_matrix_file(args[2])
        directions = filter_directions(args[4])
        found_words = find_words_in_matrix(list_of_words, matrix,
                                           directions)
        write_output_file(found_words, args[3])


if __name__ == '__main__':
    process_word_search_in_matrix(sys.argv)


