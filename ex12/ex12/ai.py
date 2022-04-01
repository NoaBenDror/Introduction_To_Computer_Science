import random

NUM_ROWS = 6
NUM_COLS = 7


class AI:
    """this is a class of a non-human player. It gets a Game object,
     and decides by its current status, about its next move.
    The logic is: random column from legal columns"""

    def __init__(self, game, player):
        self.__game = game  # initialize game object
        self.__player = player  # initialize player number

    def find_legal_move(self, timeout=None):
        """this method returns random legal move"""
        if self.__game.get_winner():  # real or tie
            raise Exception("No possible AI moves.")
        legal_lst = list()
        #  check each column if it has an empty cell
        for i in range(NUM_COLS):
            if self.__game.get_player_at(0, i) is None:
                legal_lst.append(i)  # if it is empty, add this column to list
        chosen_move = random.choice(legal_lst)  # legal_lst is not empty,
        #  because the board is not full (if it was, get.winner = 0 and then
        #  an Exception was raised)
        return chosen_move

    def get_last_found_move(self):
        pass
