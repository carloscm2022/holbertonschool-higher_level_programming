#!/usr/bin/python3
"""
First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    class inherits Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """
        private instance width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        private instance
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        private instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        private instance
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        private instance
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        private instance
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        private instance
        """
        return self.__y

    @y.setter
    def y(self, value):
        """private instance"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        returns the area value of the Rectangle instance
        """
        return self.height * self. width

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for l in range(self.y):
            print('\n', end='')
        for i in range(self.height):
            for k in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            if i != self.height - 1:
                print()
        print()

    def __str__(self):
        """
        str
        """
        return('[Rectangle] ({}) {}/{} - {}/{}'
               .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        dictionary
        """
        dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return(dict)
