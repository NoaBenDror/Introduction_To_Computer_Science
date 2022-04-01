NUM_ROWS = 7
NUM_COLS = 7
TARGET_ROW = 3
TARGET_COL = 7
EMPTY_CELL = "_"


class Board:
    """
    a class of board - a two dimensional system of coordinates.
    """

    def __init__(self):
        self.__matrix = [[EMPTY_CELL] * NUM_COLS for i in range(NUM_ROWS)]
        self.__target = (TARGET_ROW, TARGET_COL)  # the cell a car needs
        #  to get to
        self.__cars_dictionary = {}
        self.__target_value = EMPTY_CELL  # the value inside the cell a car
        #  needs to get to

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        printed_str = ""
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                printed_str += self.__matrix[row][col] + " "
            if row == TARGET_ROW:
                printed_str += self.__target_value
            printed_str += "\n"
        return printed_str

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cells_lst = []
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                cells_lst.append((row, col))
        cells_lst.append((TARGET_ROW, TARGET_COL))  # adds target cell
        return cells_lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        # assuming legal moves considering the board's limits only
        possible_moves_lst = []
        for car in self.__cars_dictionary.values():  # the actual car object
            possible_moves = car.possible_moves()
            for movekey in possible_moves:
                if self.__is_move_legal(car, movekey):
                    possible_moves_lst.append((car.get_name(), movekey,
                                               possible_moves[movekey]))
        return possible_moves_lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        return TARGET_ROW, TARGET_COL

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if coordinate[0] == TARGET_ROW and coordinate[1] == TARGET_COL:
            if self.__target_value == EMPTY_CELL:  # target cell is empty
                return None
            else:
                return self.__target_value  # target cell isn't empty
        if self.__matrix[coordinate[0]][coordinate[1]] == EMPTY_CELL:
            return None
        else:
            return self.__matrix[coordinate[0]][coordinate[1]]

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        car_coord_lst = car.car_coordinates()
        for c in car_coord_lst:
            # check we are inside the board's limits
            if c[0] < 0 or c[0] >= NUM_ROWS or c[1] < 0 or c[1] >= NUM_COLS:
                return False
            # check that the cell is free
            if self.__matrix[c[0]][c[1]] != EMPTY_CELL:
                return False
        # all cells available - add the car
        self.__cars_dictionary[car.get_name()] = car
        for c in car_coord_lst:
            self.__matrix[c[0]][c[1]] = car.get_name()  # change empty cell
            #  to car name that was added
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        car = self.__cars_dictionary[name]
        # check if legal to move the car
        if not self.__is_move_legal(car, movekey):
            return False
        #  empty car's cells
        coord_lst = car.car_coordinates()
        for c in coord_lst:
            row = c[0]
            col = c[1]
            self.__matrix[row][col] = EMPTY_CELL
        #  move the car
        car.move(movekey)
        #  fill the moved car's cells
        coord_lst = car.car_coordinates()
        for c in coord_lst:
            row = c[0]
            col = c[1]
            if row == TARGET_ROW and col == TARGET_COL:
                self.__target_value = car.get_name()
            else:
                self.__matrix[row][col] = car.get_name()
        return True

    def __is_move_legal(self, car, movekey):
        """this method checks whether the move is legal, considering the car's
         possible moves, board's limits, and blocking cars"""
        if movekey not in car.possible_moves():
            return False
        cells_required_empty = car.movement_requirements(movekey)
        for c in cells_required_empty:
            row = c[0]
            col = c[1]
            if row < 0 or col < 0:
                return False
            if (row >= NUM_ROWS or col >= NUM_COLS) and\
                    not (row == TARGET_ROW and col == TARGET_COL):
                return False  # we are outside of board's limits
                #  (not including target cell)
            if row == TARGET_ROW and col == TARGET_COL:
                if self.__target_value == EMPTY_CELL:
                    return True
                else:  # for safety, not supposed to get here
                    return False
            if self.__matrix[row][col] != EMPTY_CELL:
                return False  # cell not empty, movement illegal
        return True