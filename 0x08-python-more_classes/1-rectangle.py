#!/usr/bin/python3
#1-rectangle.py
"""" Defines a Rectangle class."""


class Rectangle:
    """ Represent a Rectangle."""

    def __init__(self,width = 0,height = 0):
        """initialize new recangle

        Args:
            width: width of the rectangle
            height: heigth of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width of the rectangle"""
        return self.__width
    @width.setter
    def width(self):
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("value must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get/Set height of the rectangle"""
        return sekf.__height

    @height.setter
    def height(self):
        if not isinstance(value,int):
            raise TypeError(" height must be an integer")
        if value < 0:
            raise ValueError(" value must be greater than zero")
        self.__height = value
