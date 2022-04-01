import tkinter as tk
from .ai import AI
from .game import Game
NUM_ROWS = 6
NUM_COLS = 7

WINNER_TO_TEXT = {0: "TIE ..", 1: "WINNER !!", 2: "WINNER !!"}
WINNER_TO_COLOR = {0: "grey", 1: "red", 2: "blue"}


class Gui:
    """this is a class of Graphical User Interface that presents
     the game to the user(s), and enables interaction.
     it creates, reflects, and interacts with a Game object.
     it has minimal logic, the Game object is the one responsible
     for the logic, legality etc."""
    def __init__(self, root):
        # create and initialize __game, which is responsible
        #  for the rules and logic
        self.__game = Game()
        #  create and initialize potential computer players
        self.__ai1 = AI(self.__game, 1)
        self.__ai2 = AI(self.__game, 2)

        #  create and initialize widgets
        cv = tk.Canvas(root, width=600, height=600,
                       highlightbackground='grey', background='grey')
        cv.pack(side=tk.BOTTOM, fill=tk.BOTH)
        b_start = tk.Button(root, width=14, height=1, text="START NEW GAME",
                            font=("Helvetica", 10), bg="yellow",
                            command=self.start_game_callback)
        b_start.pack(side=tk.TOP, fill=tk.BOTH)
        player1 = tk.Label(root, width=8, height=2, text="player 1",
                           font=("Helvetica", 15), background='red')
        player1.pack(side=tk.LEFT, fill=tk.BOTH)
        player2 = tk.Label(root, width=8, height=2, text="player 2",
                           font=("Helvetica", 15), background='blue')
        player2.pack(side=tk.RIGHT, fill=tk.BOTH)

        # widgets for choosing players ("Human" is the default)
        self.p1 = tk.StringVar()
        choice1_comp = tk.Radiobutton(root, text="Computer", variable=self.p1,
                                      value="Computer",
                                      command=self.player1_choice_callback)
        choice1_human = tk.Radiobutton(root, text="Human", variable=self.p1,
                                       value="Human",
                                       command=self.player1_choice_callback)
        self.p1.set("Human")
        choice1_comp.pack(side=tk.LEFT)
        choice1_human.pack(side=tk.LEFT)
        self.p2 = tk.StringVar()
        choice2_comp = tk.Radiobutton(root, text="Computer", variable=self.p2,
                                      value="Computer",
                                      command=self.player2_choice_callback)
        choice2_human = tk.Radiobutton(root, text="Human", variable=self.p2,
                                       value="Human",
                                       command=self.player2_choice_callback)
        self.p2.set("Human")
        choice2_human.pack(side=tk.RIGHT)
        choice2_comp.pack(side=tk.RIGHT)

        self.winning = tk.Label(root, width=13, height=2, text="WINNER !!!",
                           font=("Helvetica", 15))

        #  images for board and column arrows

        self.img_grey_arrow = tk.PhotoImage(file="ex12/greyArrow.png")
        self.img_grey_arrow = self.img_grey_arrow.subsample(2, 2)

        self.img_red_arrow = tk.PhotoImage(file="ex12/redArrow.png")
        self.img_red_arrow = self.img_red_arrow.subsample(2, 2)

        self.img_blue_arrow = tk.PhotoImage(file="ex12/blueArrow.png")
        self.img_blue_arrow = self.img_blue_arrow.subsample(2, 2)

        self.img_circle_white = tk.PhotoImage(file="ex12/white4.png")
        self.img_circle_white = self.img_circle_white.subsample(3, 3)

        self.img_circle_blue = tk.PhotoImage(file="ex12/blue4.png")
        self.img_circle_blue = self.img_circle_blue.subsample(3, 3)

        self.img_circle_red = tk.PhotoImage(file="ex12/red4.png")
        self.img_circle_red = self.img_circle_red.subsample(3, 3)

        self.img_win_red = tk.PhotoImage(file="ex12/winningRed.png")
        self.img_win_red = self.img_win_red.subsample(3, 3)

        self.img_win_blue = tk.PhotoImage(file="ex12/winningBlue.png")
        self.img_win_blue = self.img_win_blue.subsample(3, 3)

        #  board widgets (arranged as matrix). reflects __game board
        cv1 = tk.Canvas(cv, width=500, height=500,
                        highlightbackground='grey', bg='grey')
        cv1.pack(side=tk.BOTTOM)
        self.board_lst = [[None] * NUM_COLS for i in range(NUM_ROWS)]
        #  widgets of "arrows" above columns, reflecting current player and
        #  column legality
        self.arrow_lst = []
        for c in range(NUM_COLS):
            col = tk.Canvas(cv1, width=100, height=400,
                            highlightbackground='white', bg='white')
            b = tk.Button(col, image=self.img_red_arrow,
                          command=lambda lc=c: self.__chose_col_callback(lc))
            self.arrow_lst.append(b)
            col.pack(side=tk.LEFT)
            b.pack(side=tk.TOP)

            for r in range(NUM_ROWS):
                label_img = tk.Label(col, image=self.img_circle_blue)
                self.board_lst[r][c] = label_img
                label_img.pack(side=tk.TOP)

        self.__root = root
        self.__update()  # updates gui by the __game status

    def player1_choice_callback(self):
        self.__update()
        if self.__game.get_current_player() == 1 and\
                self.p1.get() == "Computer":
            self.__handle_ai_move()

    def player2_choice_callback(self):
        self.__update()
        if self.__game.get_current_player() == 2 and \
                self.p2.get() == "Computer":
            self.__handle_ai_move()

    def __chose_col_callback(self, col):
        """this method is called when a column is chosen by a player
        (human or computer). if legal (actually called only if legal) -
        calls __game to make the move, and updates the GUI """
        # this next line will be true, because if not, the button is disabled
        if self.__game.is_col_legal_for_move(col):
            self.__game.make_move(col)  # call __game to make the move
            self.__update()
            #  delay and continue handling, if after the move, it's a Computer
            #  player's turn
            if ((self.__game.get_current_player() == 1
                 and self.p1.get() == "Computer") or
                (self.__game.get_current_player() == 2
                 and self.p2.get() == "Computer")):
                self.__root.after(1000, self.__handle_ai_move)

    def __handle_ai_move(self):
        """this method is called when it's a computer player's turn:
        get the column from ai object, and call __chose_col_callback"""
        if not self.__game.is_game_over():
            if self.__game.get_current_player() == 1:
                ai_col = self.__ai1.find_legal_move()  # get move from ai
                self.__chose_col_callback(ai_col)      # and choose it
            elif self.__game.get_current_player() == 2:
                ai_col = self.__ai2.find_legal_move()  # get move from ai
                self.__chose_col_callback(ai_col)      # and choose it

    def __update(self):
        """this method updates the GUI according to __game status. it is
        called in start_game_callback and after each move """
        #  place the right disc according to __game board
        self.winning.pack_forget()
        for c in range(NUM_COLS):
            for r in range(NUM_ROWS):
                player = self.__game.get_player_at(r, c)
                if player == 1:
                    self.board_lst[r][c].config(image=self.img_circle_red)
                elif player == 2:
                    self.board_lst[r][c].config(image=self.img_circle_blue)
                else:
                    self.board_lst[r][c].config(image=self.img_circle_white)

        #  disable arrow in columns in which move is illegal
        #  (__game knows this logic):
        #  color by player 1/2/illegal, enable/disable by
        #  legal/illegal + human/computer
        game_current_player = self.__game.get_current_player()
        for c in range(NUM_COLS):
            if not self.__game.is_col_legal_for_move(c):
                self.arrow_lst[c].config(image=self.img_grey_arrow)
                self.arrow_lst[c].config(state=tk.DISABLED)
            else:
                if game_current_player == 1:
                    self.arrow_lst[c].config(image=self.img_red_arrow)
                    if self.p1.get() == "Human":
                        self.arrow_lst[c].config(state=tk.NORMAL)
                    else:
                        self.arrow_lst[c].config(state=tk.DISABLED)
                elif game_current_player == 2:
                    self.arrow_lst[c].config(image=self.img_blue_arrow)
                    if self.p2.get() == "Human":
                        self.arrow_lst[c].config(state=tk.NORMAL)
                    else:
                        self.arrow_lst[c].config(state=tk.DISABLED)
        #  if game is over
        if self.__game.is_game_over():
            winner = self.__game.get_winner()
            self.winning.config(bg=WINNER_TO_COLOR[winner],
                                text=WINNER_TO_TEXT[winner],
                                font=("Helvetica", 10))
            self.winning.pack(side=tk.LEFT, fill=tk.BOTH)
            #  if game is over with a winner
            if winner == 1 or winner == 2:
                winner_to_image = {1: self.img_win_red, 2: self.img_win_blue}
                win_lst = self.__game.get_winning_seq_list()
                for rc in win_lst:
                    self.board_lst[rc[0]][rc[1]].config(
                        image=winner_to_image[winner])

    def start_game_callback(self):
        """this method is called when the user requests to start a new game"""
        # create and initialize new __game
        self.__game = Game()
        #  create and initialize new potential computer players
        self.__ai1 = AI(self.__game, 1)
        self.__ai2 = AI(self.__game, 2)

        self.__update()
        if self.__game.get_current_player() == 1 and\
                self.p1.get() == "Computer":  # first player is the computer
            self.__handle_ai_move()