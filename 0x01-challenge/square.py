#!/usr/bin/python3

class Square:
    def __init__(self, width=0, height=0):
        """
        Initialize the Square object with optional width and height.
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """
        Calculate and return the area of the square.
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Calculate and return the perimeter of the square.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the Square object.
        """
        return f"{self.width}/{self.height}"

if __name__ == "__main__":
    # Create a Square object with specified width and height
    s = Square(width=12, height=9)

    print(s)

    print("Area:", s.area_of_my_square())

    print("Perimeter:", s.perimeter_of_my_square())
