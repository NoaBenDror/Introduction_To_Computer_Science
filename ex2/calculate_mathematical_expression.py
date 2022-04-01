def calculate_mathematical_expression(num1, num2, func):
    """a function that gets two numbers,
     and a mathematical operation, and returns the result"""
    if func == "+":
        return num1+num2
    if func == "-":
        return num1-num2
    if func == "*":
        return num1*num2
    if func == "/":
        if num2 == 0:  # no division by 0
            return None
        return num1/num2
    return None  # if the operation is not one of the four operations above


def calculate_from_string(math_function):
    """a function that gets a mathematical expression
    as string, with spaces, and transforms each value to its type. then,
    calculates it using the calculate_mathematical_expression function"""
    first_num, operation, second_num = (math_function.split())  # splits the
    # string to three strings
    return calculate_mathematical_expression(float(first_num),
                                             float(second_num), operation)
