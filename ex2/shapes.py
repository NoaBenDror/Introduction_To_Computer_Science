import math
MESSAGE_INPUT_SHAPE = "Choose shape (1=circle, 2=rectangle, 3=triangle): "
CHOICE_CIRCLE = "1"
CHOICE_RECTANGLE = "2"
CHOICE_TRIANGLE = "3"


def circle_area(rad):
    return math.pi * math.pow(rad, 2)


def rectangle_area(ed1, ed2):
    return ed1 * ed2


def triangle_area(tri_leg):
    return (math.sqrt(3) / 4) * math.pow(tri_leg, 2)


def shape_area():
    """a function that gets as user's input a shape
     and its attributes and calculates its area"""
    shape = input(MESSAGE_INPUT_SHAPE)
    if shape == CHOICE_CIRCLE:  # the shape the user chooses is a circle
        radius = float(input())
        return circle_area(radius)
    if shape == CHOICE_RECTANGLE:  # the shape the user chooses is a rectangle
        edge1 = float(input())
        edge2 = float(input())
        return rectangle_area(edge1, edge2)
    if shape == CHOICE_TRIANGLE:  # the shape the user chooses is a triangle
        tri_edge = float(input())
        return triangle_area(tri_edge)
    return None  # the user didn't choose one of the following options:
    #  1,2 or 3
