"""File to define River class."""

__author__ = "730665331"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Setting up the river class."""
    
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checks the age to see the fish and bears that survive."""
        surviving_Fish: list[self.fish] = []
        surviving_Bears: list[self.bears] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_Fish.append(fish)
        for number in self.bears:       
            if number.age <= 5:
                surviving_Bears.append(number)
        self.fish = surviving_Fish
        self.bears = surviving_Bears
    
    def remove_fish(self, amount: int) -> None:
        """Remove fish when called."""
        i = 0
        while i < amount and i < len(self.fish):
            self.fish.pop(0)
            i += 1
        
    def bears_eating(self) -> None:
        """Initialize bear eating 3 fish."""
        for count in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                count.eat(3)
    
    def check_hunger(self) -> None:
        """If hungerscore is below 0, bear dies."""
        surviving_Bears: list[self.bears] = []
        for amount in self.bears:
            if amount.hunger_score < 0:
                surviving_Bears.append(amount)
        self.bears = surviving_Bears
        
    def repopulate_fish(self) -> None:
        """Offsprings of fish pairs."""
        n: int = len(self.fish)
        pairs: int = (n // 2) * 4
        i = 0
        while i < pairs:
            child = Fish()
            self.fish.append(child)
            i += 1
        
    def repopulate_bears(self) -> None:
        """Offsprings of bear pairs."""
        n: int = len(self.bears)
        pairs: int = n // 2
        i = 0
        while i < pairs:
            new = Bear()
            self.bears.append(new)
            i += 1
    
    def view_river(self) -> None:
        """Shows the day, fish population, and bear population."""
        x = self.day
        y = len(self.fish)
        z = len(self.bears)
        print(f"~~~ Day {x}: ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Sets one week as 7 days."""
        for _ in range(7):
            self.one_river_day()
