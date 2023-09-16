#/usr/bin/python3
"""it defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """It represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """it initializes a new square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """it gets the size of a square"""
        return self.width
    @size.setter
    def size(self, value):
        """it sets the size of a squre"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """it assigns argument to attribute"""
        if args and len(args) != 0:
            c = 0
            for arg in args:
                if c == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = arg
                elif c == 1:
                    self.size = arg
                elif c == 2:
                    self.x = arg
                elif c == 3:
                    self.y = arg
                c += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        id = value
                elif key == "size":
                    size = value
                elif key == "x":
                    x = value
                elif key == "y":
                    y = value

    def to_dictionary(self):
        """it returns dictionay representation of square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
            }
            

    def __str__(self):
        """it prints string representation of square"""
        return "[square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
