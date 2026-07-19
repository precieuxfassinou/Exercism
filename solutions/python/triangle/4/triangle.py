""" Module to determine the nature of an triangle """

def is_valid_triangle(sides):
    """ function to determine if the triangle is valid """
    side_one = sides[0]
    side_two = sides[1]
    side_three = sides[2]
    
    if side_one > 0 and side_two > 0 and side_three > 0:
        if side_one + side_two >= side_three and side_two + side_three >= side_one and  side_one + side_three >= side_two:
            return True
    return False
    
def equilateral(sides):
    """ function to determine if the triangle is equilateral """
    if is_valid_triangle(sides):
        side_one, side_two, side_three = sides
        if side_one == side_two == side_three:
            return True
    return False

equilateral([1, 2, 3])

def isosceles(sides):
    """ function to determine if the triangle is isosceles """
    if is_valid_triangle(sides):
        side_one, side_two, side_three = sides
        if (side_one == side_two)or (side_two == side_three) or (side_three == side_one) or (side_one == side_two == side_three):
            return True
    return False

isosceles([1, 2, 3])

def scalene(sides):
    """ function to determine if the triangle is scalene """
    if is_valid_triangle(sides):
        side_one, side_two, side_three = sides
        if side_one != side_two and side_two != side_three and side_one != side_three:
            return True
    return False
    
scalene([1, 2, 3])