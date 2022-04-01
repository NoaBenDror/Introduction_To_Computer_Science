import math
MESSAGE_INSERT = "Insert coefficients a, b, and c: "
MESSAGE_NO_SOLUTION = "The equation has no solutions"
MESSAGE_ONE_SOLUTION = "The equation has 1 solution: "
MESSAGE_TWO_SOLUTIONS = "The equation has 2 solutions: "


def quadratic_equation(a, b, c):
    """ a function that gets 3 coefficients
    and calculates a quadratic equation"""
    sq = math.pow(b, 2) - 4 * a * c  # this is what's inside the root
    if sq == 0:  # if sq equals 0, it means the equation has 1 solution
        first_solution = -b / (2 * a)
        second_solution = None
    elif sq < 0:  # if sq is below 0, it means the equation has no solutions
        first_solution = None
        second_solution = None
    else:  # if sq is above 0, the equation has 2 solutions
        first_solution = (-b + math.sqrt(sq)) / (2 * a)
        second_solution = (-b - math.sqrt(sq)) / (2 * a)

    return first_solution, second_solution


def quadratic_equation_user_input():
    """a function that gets as user's input three coefficients
     and prints the solution for quadratic equation
     using the quadratic_equation function"""
    a, b, c = input(MESSAGE_INSERT).split()  # user inserts
    #  the three coefficients, splits the coefficients to three strings
    solution1, solution2 = quadratic_equation(float(a), float(b), float(c))
    # returns the solution according to the user's input
    if solution1 is None and solution2 is None:
        print(MESSAGE_NO_SOLUTION)
    elif solution1 is not None and solution2 is None:
        print(MESSAGE_ONE_SOLUTION + str(solution1))
    else:  # we can assume that the option that solution1 is None
        #  and solution2 is not None - can't occur
        print(MESSAGE_TWO_SOLUTIONS + str(solution1) + " and " + str(solution2))
