"""Rectangular and polar coordinates representation utility."""
from math import *
from taurapoint import *

def main():
    test = ""
    ##### CREATING #####
    # create passing x and y
    test = test = "create passing x and y"
    print("test:", test)
    p1 = Point2(0, 1)
    try:
        assert p1.x == 0
        assert p1.y == 1
        assert p1.r == 1
        assert p1.a == round(pi/2,16)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    print("test:", test)
    p1 = Point2(1, 0)
    try:
        assert p1.x == 1
        assert p1.y == 0
        assert p1.r == 1
        assert p1.a == 0
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    # create with x and y as a tuple
    test = "create with x and y as a tuple"
    print("test:", test)
    p1 = Point2((0, 1))
    try:
        assert p1.x == 0
        assert p1.y == 1
        assert p1.r == 1
        assert p1.a == round(pi/2,16)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    # create from another point
    test = "create from another point"
    print("test:", test)
    p2 = Point2(p1)
    try:
        assert p2.x == 0
        assert p2.y == 1
        assert p2.r == 1
        assert p2.a == round(pi/2,16)    
        print("passed!")
    except Exception as e:
        print("ERROR",e, p2)

    # create with no arguments
    test = "create with no arguments"
    print("test:", test)
    p1 = Point2()
    try:
        assert p1.x == 0
        assert p1.y == 0
        assert p1.r == 0
        assert p1.a == 0
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    ##### SETTING #####
    # set rectangular coordinates x and y
    test = "set rectangular coordinates x and y"
    print("test:", test)
    p1 = Point2().rect(0, 1)
    try:
        assert p1.x == 0
        assert p1.y == 1
        assert p1.r == 1
        assert p1.a == round(pi/2,16)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    # set rectangular coordinates x and y as a tuple
    test = "set rectangular coordinates x and y as a tuple"
    print("test:", test)
    p1 = Point2().rect((0, 1))
    try:
        assert p1.x == 0
        assert p1.y == 1
        assert p1.r == 1
        assert p1.a == round(pi/2,16)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    # set polar coordinates r and a
    test = "set polar coordinates r and a"
    print("test:", test)
    p1 = Point2().polar(1, round(pi/2,16))
    try:
        assert p1.x == 0
        assert p1.y == 1
        assert p1.r == 1
        assert p1.a == round(pi/2,16)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    # set polar coordinates r and a as a tuple
    test = "set polar coordinates r and a as a tuple"
    print("test:", test)
    p1 = Point2().polar((1, round(pi/2,16)))
    try:
        assert p1.x == 0
        assert p1.y == 1
        assert p1.r == 1
        assert p1.a == round(pi/2,16)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    test = "set attribute x"
    print("test:", test)
    p1 = Point2()
    p1.x = 1
    try:
        assert p1.polar() == (1, 0)
        assert p1.rect()  == (1, 0)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    test = "set attribute y"
    print("test:", test)
    p1 = Point2()
    p1.y = 1
    try:
        assert p1.polar() == (1, round(pi/2,16))
        assert p1.rect()  == (0, 1)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    test = "set attribute r"
    print("test:", test)
    p1 = Point2()
    p1.r = 1
    try:
        assert p1.polar() == (1, 0)
        assert p1.rect()  == (1, 0)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    test = "set attribute a"
    print("test:", test)
    p1 = Point2()
    p1.r = 1
    p1.a = round(pi/2,16)
    try:
        assert p1.polar() == (1, round(pi/2,16))
        assert p1.rect()  == (0, 1)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)


    ##### GETTING #####
    test = "### GETTING #####"
    print("test:", test)
    try:
        assert p1.polar() == (1, round(pi/2,16))
        assert p1.rect()  == (0, 1)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    ##### OPERATIONS ####
    test = "vector + vector"
    print("test:", test)
    p1 = Point2(1, 0)
    p2 = Point2(0, 1)
    try:
        assert (p1 + p2).rect() == (1, 1)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    test = "vector - vector"
    print("test:", test)
    p1 = Point2(1, 0)
    p2 = Point2(0, 1)
    try:
        assert (p1 - p2).rect() == (1, -1)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    test = "vector += vector"
    print("test:", test)
    p1 = Point2(1, 0)
    p2 = Point2(0, 1)
    p1 += p2
    try:
        assert p1.rect() == (1, 1)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    test = "vector -= vector"
    print("test:", test)
    p1 = Point2(1, 0)
    p2 = Point2(0, 1)
    p1 -= p2
    try:
        assert p1.rect() == (1, -1)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)

    test = "vector * scalar"
    print("test:", test)
    p1 = Point2(1, 0)
    n = 2
    try:
        assert (p1 * n).rect() == (2, 0)
        print("passed!")
    except Exception as e:
        print("ERROR",e, p1)







if __name__ == '__main__':
    main()