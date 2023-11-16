"""File to define Fish class"""

__author__ = "730665331"

class Fish:

    age: int
    
    def __init__(self):
        self.age: int = 0
        return None
    
    def one_day(self) -> None:
        self.age += 1