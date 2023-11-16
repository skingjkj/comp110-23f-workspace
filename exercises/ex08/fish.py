"""File to define Fish class."""

__author__ = "730665331"


class Fish:
    """Setting up the fish class."""
    
    age: int
    
    def __init__(self) -> None:
        """Initializing the age for fish."""
        self.age: int = 0
    
    def one_day(self) -> None:
        """Initializing +1 age per day."""
        self.age += 1