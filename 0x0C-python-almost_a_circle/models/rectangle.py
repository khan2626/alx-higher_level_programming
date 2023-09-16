#!/usr/bin/python3
"""It defines a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """It represents rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """it gets the width"""
        return self.__width
    @width.setter
    def width(self, value):
        """it sets the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """it gets the height of rectangle"""
        return self.__height
    @height.setter
    def height(self, value):
        """it set the height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """it gets x"""
        return self.__x
    @x.setter
    def x(self, value):
        """it sets x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """it gets y"""
        return self.__y
    @y.setter
    def y(self, value):
        """it sets y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """computes area of rectangle"""
        return self.width * self.height

    def display(self):
        """It prints rectangle with # char"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]

        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]

        [print("#", end="") for w in range(self.width)]
        print("")

    def update(self, *args, **kwargs):
        """It assign argument to attributes"""
        if args and len(args) != 0:
            c = 0
            for arg in args:
             if c == 0:
                 if arg is None:
                     self.__init__(self,width, self.height, self.x, self.y)
                 else:
                     self.id = arg
             elif c == 1:
                 self.width = arg
             elif c == 2:
                 self.height = arg
             elif c == 3:
                 self.x = arg
             elif c == 4:
                 self.y = arg
            c += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.wdth, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """It returns dictionary of rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
                    

    def __str__(self):
        """it print string to stdout"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
