class Car:
    """
    a class of car - has name, length, location, orientation,
    and various methods.
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col)
         location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coordinates_lst = []
        if self.__orientation == 0:
            for i in range(self.__length):
                coordinates_lst.append((self.__location[0]+i,
                                        self.__location[1]))
        else:  # orientation is 1
            for i in range(self.__length):
                coordinates_lst.append((self.__location[0],
                                        self.__location[1]+i))
        return coordinates_lst

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
         permitted by this car.
        """
        if self.__orientation == 0:
            movekey_to_desc = {"u": "cause the car to move one cell up",
                               "d": "cause the car to move one cell down"}
        else:  # orientation is 1
            movekey_to_desc = {"r": "cause the car to move one cell right",
                               "l": "cause the car to move one cell left"}
        return movekey_to_desc

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
        this move to be legal.
        """
        requirements_lst = []
        if movekey == "r":
            requirements_lst.append((self.__location[0],
                                     self.__location[1] + self.__length))
        elif movekey == "l":
            requirements_lst.append((self.__location[0],
                                     self.__location[1] - 1))
        elif movekey == "u":
            requirements_lst.append((self.__location[0] - 1,
                                     self.__location[1]))
        elif movekey == "d":
            requirements_lst.append((self.__location[0] + self.__length,
                                     self.__location[1]))
        return requirements_lst

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if (movekey == "u" or movekey == "d") and self.__orientation == 1:
            # horizontal car can't move up or down
            return False
        if (movekey == "r" or movekey == "l") and self.__orientation == 0:
            # vertical car can't move right or left
            return False
        # if we got here, it means the movement is legal - change the car's
        #  location according to movement
        if movekey == "u":
            self.__location = (self.__location[0]-1, self.__location[1])
        if movekey == "d":
            self.__location = (self.__location[0]+1, self.__location[1])
        if movekey == "r":
            self.__location = (self.__location[0], self.__location[1]+1)
        if movekey == "l":
            self.__location = (self.__location[0], self.__location[1]-1)
        return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
