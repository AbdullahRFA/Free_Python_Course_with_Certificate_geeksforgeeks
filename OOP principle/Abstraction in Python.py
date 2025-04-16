# {
# Driver Code Starts
# Initial Template for Python 3
from abc import ABC, abstractmethod

# } Driver Code Ends

# User function Template for python3
#  Implement both the classes here
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, c):
        self.color = c

    def get_color(self):
        return self.color

    @abstractmethod
    def get_area(self):
        pass


class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side

    def get_area(self):
        return self.side * self.side


square = Square("red", 5.0)
square.get_area()
# {
# Driver Code Starts.


if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        color = input()
        side = float(input())

        square = Square(color, side)

        # Check if 'square' is an instance of Shape (or its subclass)
        if isinstance(square, Shape):
            print(f"{square.get_color()} {square.get_area()}")
        else:
            print("square is NOT an instance of Shape.")

# } Driver Code Ends