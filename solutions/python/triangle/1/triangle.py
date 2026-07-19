def isTriange(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if a > 0 and b > 0 and c > 0:
        if a + b >= c and b + c >= a and  a + c >= b:
            return True
    return False
    
def equilateral(sides):
    if isTriange(sides):
        a, b, c = sides
        if a == b == c:
            return True
    return False

equilateral([1, 2, 3])

def isosceles(sides):
    if isTriange(sides):
        a, b, c = sides
        if (a == b)or (b == c) or (c == a) or (a == b == c):
            return True
    return False

isosceles([1, 2, 3])

def scalene(sides):
    if isTriange(sides):
        a, b, c = sides
        if a != b and b != c and a != c:
            return True
    return False
    
scalene([1, 2, 3])