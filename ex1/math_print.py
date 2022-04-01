import math


def golden_ratio():
    """a function that prints the golden ratio(15 digits precision)"""
    print((1+math.sqrt(5))/2)


def six_cubed():
    """a function that prints 6 raised to the power 3"""
    print(math.pow(6, 3))


def hypotenuse():
    """a function that prints the hypotenuse length(15 digits precision)"""
    print(math.hypot(3, 5))


def pi():
    """a function that prints the value of pi (15 digits precision)"""
    print(math.pi)


def e():
    """a function that prints the value of e(15 digits precision)"""
    print(math.e)


def triangular_area():
    """a function that prints the areas of
    isosceles and right triangles, legs 1-10"""
    print(math.pow(1, 2)/2, math.pow(2, 2)/2, math.pow(3, 2)/2,
          math.pow(4, 2)/2, math.pow(5, 2)/2, math.pow(6, 2)/2,
          math.pow(7, 2)/2, math.pow(8, 2)/2, math.pow(9, 2)/2,
          math.pow(10, 2)/2)


if __name__ == "__main__":
    golden_ratio()
    six_cubed()
    hypotenuse()
    pi()
    e()
    triangular_area()

