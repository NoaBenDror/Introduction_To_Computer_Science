import hangman_helper
UNKNOWN_LETTER = "_"  # under score
A_B_C = "abcdefghijklmnopqrstuvwxyz"
CHAR_A = 97
LETTERS_IN_ALPHABET = 26


def update_word_pattern(word, pattern, letter):
    """a function that gets a word, the current pattern and a letter,
     and returns an updated pattern that contains the letter"""
    for i in range(len(word)):
        if letter == word[i]:
            pattern = pattern[:i] + letter + pattern[i+1:]
    return pattern


def run_single_game(words_list):
    """the function runs the hangman game a single time"""
    #  initialize the game
    random_word = hangman_helper.get_random_word(words_list)
    wrong_guess_lst = list()
    pattern = UNKNOWN_LETTER * len(random_word)  # before the game starts,
    #  defining the pattern to be empty
    message_to_user = hangman_helper.DEFAULT_MSG
    error_count = 0
    already_chosen_lst = list()
    #  the game loop:
    while UNKNOWN_LETTER in pattern and\
            len(wrong_guess_lst) < hangman_helper.MAX_ERRORS:
        hangman_helper.display_state(pattern, error_count, wrong_guess_lst,
                                     message_to_user)
        user_choice = hangman_helper.get_input()
        if user_choice[0] == hangman_helper.LETTER:
            letter = user_choice[1]
            if letter not in A_B_C or len(letter) != 1:
                message_to_user = hangman_helper.NON_VALID_MSG
            elif letter in already_chosen_lst:
                message_to_user = hangman_helper.ALREADY_CHOSEN_MSG + letter
            elif letter in random_word:  # right guess
                pattern = update_word_pattern(random_word, pattern, letter)
                message_to_user = hangman_helper.DEFAULT_MSG
                already_chosen_lst.append(letter)  # adding the chosen letter
                #  to list of already chosen letters
            else:  # wrong guess
                wrong_guess_lst.append(letter)
                error_count += 1
                already_chosen_lst.append(letter)  # adding the chosen letter
                #  to list of already chosen letters
                message_to_user = hangman_helper.DEFAULT_MSG
        if user_choice[0] == hangman_helper.HINT:  # player wants a hint
            filtered_lst = filter_words_list(words_list, pattern,
                                             wrong_guess_lst)
            should_choose = choose_letter(filtered_lst, pattern)
            #  most common letter that fits the pattern
            message_to_user = hangman_helper.HINT_MSG + should_choose
            hangman_helper.display_state(pattern, error_count,
                                         wrong_guess_lst, message_to_user)
# the game ended
    if len(wrong_guess_lst) >= hangman_helper.MAX_ERRORS: # loss
        message_to_user = hangman_helper.LOSS_MSG + random_word
    if UNKNOWN_LETTER not in pattern:  # win
        message_to_user = hangman_helper.WIN_MSG
    hangman_helper.display_state(pattern, error_count, wrong_guess_lst,
                                 message_to_user, ask_play=True)  # asking the
    #  player if he would like to play again


def is_in_wrong_guess_lst(word, wrong_guess_lst):
    """a function that gets a word and a list of wrong guesses,
     and checks whether this word contains a letter
     from the list of wrong guesses"""
    for i in range(len(word)):
        if word[i] in wrong_guess_lst:
                return True
    return False


def is_letters_match(word, pattern):
    """a function that gets a word and a pattern, and checks if the letters
    in the pattern match the letters in the word.
    assuming they have the same length"""
    pattern_letters_lst = list()  # pattern letters list, for use in 2nd check
    # 1: check if each letter in pattern matches the letter in word
    for i in range(len(pattern)):
        if pattern[i] != UNKNOWN_LETTER and pattern[i] != word[i]:
            return False
        if pattern[i] != UNKNOWN_LETTER and\
                pattern[i] not in pattern_letters_lst:
            pattern_letters_lst.append(pattern[i])

    # 2: check that each letter in the word that was matched,
    #  matches in all its occurrences
    for j in range(len(word)):
        if word[j] in pattern_letters_lst and pattern[j] == UNKNOWN_LETTER:
            return False
    return True


def filter_words_list(words, pattern, wrong_guess_lst):
    """a function that gets a list of words, a pattern, and a list of
    wrong guesses, and returns a list that contains only the words
    that fit the pattern and previous guesses"""
    filtered_list = list()
    for word in words:  # traversing list of words
        if len(word) != len(pattern):  # same length
            continue  # to the next word in the list
        if is_in_wrong_guess_lst(word, wrong_guess_lst):  # if found a letter
            #  from wrong guesses in word
            continue
        if is_letters_match(word, pattern):
            filtered_list.append(word)
    return filtered_list


def check_common_letter_not_in_pattern(count_letters_lst, pattern):
    """ a function that gets a list of counters(related to letters),
    and a pattern, returns the letter with the maximal counter,
    excluding pattern letters """
    max_times = 0  # meanwhile, expected to be updated
    common_letter = ""  # meanwhile, expected to be updated with letter
    for i in range(len(count_letters_lst)-1):
        if count_letters_lst[i] > max_times and\
                index_to_letter(i) not in pattern:
            max_times = count_letters_lst[i]
            common_letter = index_to_letter(i)
    return common_letter


def choose_letter(words, pattern):
    """a function that gets list of words (that matches this pattern),
     and a pattern, and returns the most common letter in the list"""
    count_letters_lst = list()  # a list of letter counters (counts for each
    # letter the number of times that it appears in list of words)
    for i in range(LETTERS_IN_ALPHABET):
        count_letters_lst.append(0)  # before traversing list of words,
        #  zeroing each letter

    for word in words:  # traversing all the letters in list of words,
        #  and for each letter - update its occurrence counter
        for char in word:
            i_of_letter = letter_to_index(char)
            count_letters_lst[i_of_letter] += 1  # updates the counter

    return check_common_letter_not_in_pattern(count_letters_lst, pattern)


def letter_to_index(letter):
    """return the index of the given letter in an alphabet list"""
    return ord(letter.lower()) - CHAR_A


def index_to_letter(index):
    """return the letter corresponding to the given index"""
    return chr(index + CHAR_A)


def main():
    words_list = hangman_helper.load_words()
    play = True
    while play:
        run_single_game(words_list)
        if not hangman_helper.get_input()[1]:
            play = False


if __name__ == '__main__':
    hangman_helper.start_gui_and_call_main(main)
    hangman_helper.close_gui()
