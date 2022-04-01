NUM_ROWS = 6
NUM_COLS = 7
EMPTY_CELL = None
WIN_SEQ = 4  # this number represents the length of discs sequence for winning


class Game:
    """This is a class of the game. It (and only it) is responsible for the
    rules and the logic of the game, checks legality, maintains who is the
    the current player, declares winning, etc.
    The status changes by make_move() from outside, and is returned by several
    "get" methods"""

    def __init__(self):
        #  initialize the board, None in all cells
        self.__board = [[EMPTY_CELL] * NUM_COLS for i in range(NUM_ROWS)]
        #  initialize current player to player number 1
        self.__current_player = 1
        #  initialize winner as None
        self.__winner = None
        #  initialize the winning list (the 4 cells)
        self.__winning_seq_list = []

    def make_move(self, column):
        """this method gets the chosen column to drop the disc in. if the
        column is legal (inside the board, and has an empty cell), "drops" the
        disc. otherwise, raises an Exception"""
        if column < 0 or column >= NUM_COLS:  # outside the board
            raise Exception("Illegal move.")
        if self.__winner is not None:  # game ended
            raise Exception("Illegal move.")
        move_succ = False
        # traverse the column's rows from bottom to top
        for i in range(NUM_ROWS-1, -1, -1):
            if self.__board[i][column] is None:  # found empty cell
                self.__board[i][column] = self.__current_player  # "drop" disc
                move_succ = True
                #  update winner status after movement
                self.__check_four_in_a_row(i, column,
                                           self.get_current_player())
                self.__switch_current_player()
                break  # no need to continue the loop, already dropped disc
        if not move_succ:  # means the column was completely full
            raise Exception("Illegal move.")

    def is_col_legal_for_move(self, col):
        """this method gets a col, and checks whether it's full(assuming
        col is in board)"""
        return self.__board[0][col] is None and self.__winner is None

    def __check_four_in_a_row(self, last_move_row, last_move_col,
                              last_player):
        """this method gets row and col of last placement of the disc, and
        which player made the move, and checks whether last move caused
        winning (assuming legal move! called only after an actual move)"""
        self.__winning_seq_list = self.__check_row(last_move_row,
                                                   last_move_col,
                                                   last_player)
        if self.__winning_seq_list:
            self.__winner = last_player
            return  # we have a winner!

        self.__winning_seq_list = self.__check_col(last_move_row,
                                                   last_move_col,
                                                   last_player)
        if self.__winning_seq_list:
            self.__winner = last_player
            return  # we have a winner!

        self.__winning_seq_list = self.__check_diag_1(last_move_row,
                                                      last_move_col,
                                                      last_player)
        if self.__winning_seq_list:
            self.__winner = last_player
            return  # we have a winner!

        self.__winning_seq_list = self.__check_diag_2(last_move_row,
                                                      last_move_col,
                                                      last_player)
        if self.__winning_seq_list:
            self.__winner = last_player
            return  # we have a winner!

        for i in range(NUM_COLS):  # check if the board is full
            if self.__board[0][i] is None:
                return  # board not full, the game continues

        self.__winner = 0  # if we got here, it's a tie

    def __check_row(self, last_move_row, last_move_col, last_player):
        """this method gets row and col of last placement of the disc, and
        which player made the move, and checks whether last move caused
        winning by completing 4 in the row"""
        sequence_list = list()
        c = last_move_col
        # check left direction
        while c >= 0:  # inside board
            if self.__board[last_move_row][c] == last_player:
                sequence_list.append((last_move_row, c))
            else:
                break  # no more matching in this direction
            if len(sequence_list) == WIN_SEQ:
                return sequence_list  # found 4 in a row
            c -= 1

        # check right direction (continue filling sequence list)
        c = last_move_col + 1
        while c < NUM_COLS:  # inside board
            if self.__board[last_move_row][c] == last_player:
                sequence_list.append((last_move_row, c))
            else:
                break  # no more matching in this direction
            if len(sequence_list) == WIN_SEQ:
                return sequence_list  # found 4 in a row
            c += 1
        if len(sequence_list) == WIN_SEQ:
            return sequence_list
        return []

    def __check_col(self, last_move_row, last_move_col, last_player):
        """this method gets row and col of last placement of the disc, and
        which player made the move, and checks whether last move caused
        winning by completing 4 in the column"""
        sequence_list = list()
        r = last_move_row
        # check down (this is the top disc - no discs above)
        while r < NUM_ROWS:  # inside board
            if self.__board[r][last_move_col] == last_player:
                sequence_list.append((r, last_move_col))
            else:
                break  # no more matching in this direction
            if len(sequence_list) == WIN_SEQ:
                return sequence_list  # found 4 in a row
            r += 1
        if len(sequence_list) == WIN_SEQ:
            return sequence_list
        return []

    def __check_diag_1(self, last_move_row, last_move_col, last_player):
        """this method gets row and col of last placement of the disc, and
        which player made the move, and checks whether last move caused
        winning by completing a diagonal"""
        sequence_list = list()
        r = last_move_row
        c = last_move_col
        # check left up direction
        while r >= 0 and c >= 0:  # inside board
            if self.__board[r][c] == last_player:
                sequence_list.append((r, c))
            else:
                break  # no more matching in this direction
            if len(sequence_list) == WIN_SEQ:
                return sequence_list  # found 4 in a row
            r -= 1
            c -= 1

        # check down right direction (continue filling sequence list)
        r = last_move_row + 1
        c = last_move_col + 1
        while r < NUM_ROWS and c < NUM_COLS:  # inside board
            if self.__board[r][c] == last_player:
                sequence_list.append((r, c))
            else:
                break  # no more matching in this direction
            if len(sequence_list) == WIN_SEQ:
                return sequence_list  # found 4 in a row
            r += 1
            c += 1
        if len(sequence_list) == WIN_SEQ:
            return sequence_list
        return []

    def __check_diag_2(self, last_move_row, last_move_col, last_player):
        """this method gets row and col of last placement of the disc, and
        which player made the move, and checks whether last move caused
        winning by completing a diagonal"""
        sequence_list = list()
        r = last_move_row
        c = last_move_col
        # check right up direction
        while r >= 0 and c < NUM_COLS:  # inside board
            if self.__board[r][c] == last_player:
                sequence_list.append((r, c))
            else:
                break  # no more matching in this direction
            if len(sequence_list) == WIN_SEQ:
                return sequence_list  # found 4 in a row
            r -= 1
            c += 1

        # check down left direction (continue filling sequence list)
        r = last_move_row + 1
        c = last_move_col - 1
        while r < NUM_ROWS and c >= 0:  # inside board
            if self.__board[r][c] == last_player:
                sequence_list.append((r, c))
            else:
                break  # no more matching in this direction
            if len(sequence_list) == WIN_SEQ:
                return sequence_list  # found 4 in a row
            r += 1
            c -= 1
        if len(sequence_list) == WIN_SEQ:
            return sequence_list
        return []

    def get_winner(self):
        """this method returns winning status"""
        return self.__winner

    def get_winning_seq_list(self):
        """this method returns winning sequence list"""
        return self.__winning_seq_list

    def get_player_at(self, row, col):
        """this method gets row and column and returns what's inside the cell-
        one of the players (1 or 2) or None"""
        if row < 0 or row >= NUM_ROWS or col < 0 or col >= NUM_COLS:
            raise Exception("Illegal location.")  # outside of board
        else:
            return self.__board[row][col]

    def get_current_player(self):
        """this method returns which player's turn is it"""
        return self.__current_player

    def __switch_current_player(self):
        """this method switches current player"""
        if self.__current_player == 1:
            self.__current_player = 2
        else:
            self.__current_player = 1

    def is_game_over(self):
        """this method returns whether the game is over"""
        return self.__winner is not None
