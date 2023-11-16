"""File to define Bear class."""

__author__ = "730665331"


class Bear:
    """Class for bears."""    

    age: int
    hunger_score: int
    
    def __init__(self) -> None:
        """Initializing age and hungerscore."""
        self.age = 0
        self.hunger_score = 0
        
    def one_day(self) -> None:
        """Initializing day."""
        self.age += 1
        self.hunger_score -= 1
    
    def eat(self, num_fish: int) -> None:
        """Initializing eating."""
        self.hunger_score += num_fish