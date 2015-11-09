#############################################
# Copyright (c) 2015 Fabricio JC Montenegro #
# 8th november 2015                         #
# Version 1.0                               #
#############################################

"""Rectangular and polar coordinates representation utility."""
from math import *

__all__ = ["Point2"]

pi = round(pi, 16)

class Point2:
    """
    This class represents a 2D vector and stores the rectangular and polar 
    coordinates at the same time avoiding the need of convertion
    """
    def __init__(self, x=None, y=None):
        self.__dict__['x'] = 0.0
        self.__dict__['y'] = 0.0
        self.__dict__['r'] = 0.0
        self.__dict__['a'] = 0.0

        if x == None:
            pass
        elif type(x) == Point2:
            self.__dict__['x'] = x.x
            self.__dict__['y'] = x.y
            self.__dict__['r'] = x.r
            self.__dict__['a'] = x.a
        elif type(x) == tuple:
            self.__dict__['x'] = x[0]
            self.__dict__['y'] = x[1]
            self.__dict__['r'] = sqrt(self.x**2 + self.y**2)
            self.__dict__['a'] = atan2(self.y, self.x)
        elif not x==None and not y==None:
            self.__dict__['x'] = x
            self.__dict__['y'] = y
            self.__dict__['r'] = sqrt(self.x**2 + self.y**2)
            self.__dict__['a'] = atan2(self.y, self.x)
        # Python 2 hook
        elif x.__class__.__name__ == 'Point2':
            self.__dict__['x'] = x.x
            self.__dict__['y'] = x.y
            self.__dict__['r'] = x.r
            self.__dict__['a'] = x.a

    def recalc(self, fromRect=True):
        """Used internally to recalculate the values of one set of coordinates 
        when the other is changed."""
        if fromRect:
            self.__dict__['r'] = sqrt(self.x**2 + self.y**2)
            self.__dict__['a'] = atan2(self.y, self.x)
        else:
            self.__dict__['x'] = round(self.r * cos(self.a),15)
            self.__dict__['y'] = round(self.r * sin(self.a),15)
        return self

    def rect(self, x=None, y=None):
        if x == None:
            return (self.x, self.y)
        elif type(x) == tuple:
            self.__dict__['x'] = x[0]
            self.__dict__['y'] = x[1]
            self.__dict__['r'] = sqrt(self.x**2 + self.y**2)
            self.__dict__['a'] = atan2(self.y, self.x)
        elif not x==None and not y==None:
            self.__dict__['x'] = x
            self.__dict__['y'] = y
            self.__dict__['r'] = sqrt(self.x**2 + self.y**2)
            self.__dict__['a'] = atan2(self.y, self.x)

        return self

    def polar(self, r=None, a=None):
        if r == None:
            return (self.r, self.a)
        elif type(r) == tuple:
            self.__dict__['r'] = r[0]
            self.__dict__['a'] = r[1]
            self.__dict__['x'] = round(self.r * cos(self.a), 15)
            self.__dict__['y'] = round(self.r * sin(self.a), 15)
        elif not r==None and not a==None:
            self.__dict__['r'] = r
            self.__dict__['a'] = a
            self.__dict__['x'] = round(self.r * cos(self.a), 15)
            self.__dict__['y'] = round(self.r * sin(self.a), 15)

        return self

    def __setattr__(self, name, value):
        """Point2.x, Point2.y, Point2.r, Point2.a, Point2.phi -> number

        Accesses any of the member variables of Point2 to set and get them
        directly. Exemples:
        v.x = 2
        x = v.x"""
        if name == 'x' or name == 'y':
            self.__dict__[name] = value
            self.recalc()
        elif name == 'r' or name == 'a':
            self.__dict__[name] = value
            self.recalc(False)
        else:
            self.__dict__[name] = value

    def __iadd__(self, other):
        """Implements the += operation"""
        x = self.x + other.x
        y = self.y + other.y
        return Point2(x,y)

    def __isub__(self, other):
        """Implements the -= operation"""
        x = self.x - other.x
        y = self.y - other.y
        return Point2(x,y)

    def __add__(self, other):
        """Implements the + operation"""
        x = self.x + other.x
        y = self.y + other.y
        return Point2(x,y)

    def __sub__(self, other):
        """Implements the - operation"""
        x = self.x - other.x
        y = self.y - other.y
        return Point2(x,y)

    def __mul__(self, value):
        """Implements the dot (scalar) product for a vector"""
        self.r = self.__dict__['r'] = self.r * value
        return Point2(self)

    def __len__(self):
        """Makes possible to call len(vector) to get the length of 
        the vector"""
        return int(self.r)

    def __repr__(self):
        """Returns a string in a 'r(x, y) p(r, a)' format"""
        return "(rect({0}, {1}), polar({2}, {3}))".format( 
            str(self.x), str(self.y), str(self.r), str(self.a)
        )
