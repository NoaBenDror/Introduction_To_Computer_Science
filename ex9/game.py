from car import Car
from board import Board
import sys
from helper import load_json

CAR_NAMES = ["Y", "B", "O", "W", "G", "R"]  # car possible names
ORIENTATIONS = [0, 1]  # car possible orientations
LENGTHS = [2, 3, 4]  # car possible length
MOVEKEYS = ["u", "d", "r", "l"]  # car possible movements(up, down,
                                 #  right, left)


class Game:
    """
    a class of rush-hour game, which contains a board. the board is presented
    to the player, and the player moves the objects in the board.
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board

    def __single_turn(self):
        """
         The function runs one round of the game:
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.
            if the car moved to target cell, means exit, the game ends.
        """
        print(board)  # shows the board to the player
        legal_input = False
        while not legal_input:
            print("Please enter: <car_name,movement>")
            user_turn = input()  # chooses which car to move, and a movement
            user_choice = self.__pars_check_input(user_turn)  # check input
            if user_choice is None:
                print("Illegal syntax")
            else:
                car_name = user_choice[0]
                car_movement = user_choice[1]
                # check if movement is legal according to position and
                #  other cars in the board
                if board.move_car(car_name, car_movement):
                    legal_input = True  # succeeded to move the car
                    # check if the car got to target cell (exit)
                    if board.cell_content(board.target_location()) is\
                            not None:
                        print(board)
                        print("Good job! Game Over")
                        # the car did get to exit - game ends
                        return True
                else:  # can't move the car
                    print("Illegal movement")  # and do the loop again
        return False

    def __pars_check_input(self, user_turn):
        """this function checks whether the user entered a legal syntax
        according to <car_name,movement>, and according to cars in board.
        if not, return None. if syntax is legal, return a list of length 2:
        [string of car color,string of movement]"""
        if "," not in user_turn or " " in user_turn:
            return None
        user_choice = user_turn.split(",")
        if len(user_choice) != 2:  # more than one ","
            return None
        if user_choice[0] not in CAR_NAMES or user_choice[1] not in MOVEKEYS:
            return None
        pos_moves_lst = board.possible_moves()
        for m in pos_moves_lst:  # traverse possible moves
            if user_choice[0] == m[0]:  # car is in board
                return user_choice
        return None

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        end_game = False
        while not end_game:
            end_game = self.__single_turn()  # "__single_turn" returns True
            #  or False- if True a car got to exit- end the game
            # (and stop the loop). if False the player needs to keep playing


if __name__ == "__main__":
    board = Board()  # create board
    filename = sys.argv[1]
    cars_config = load_json(filename)  # dictionary of cars from json
    #  add cars to board if legal
    for name in cars_config:  # traverse keys(car names) in dictionary of cars
        length = cars_config[name][0]
        location = tuple(cars_config[name][1])
        orientation = cars_config[name][2]
        if name in CAR_NAMES and \
                length in LENGTHS and\
                orientation in ORIENTATIONS:
            car = Car(name, length, location, orientation)  # create car
            board.add_car(car)  # will only be added if location is legal
            # by board (including previous cars)

    game = Game(board)  # create game
    game.play()  #  play the game