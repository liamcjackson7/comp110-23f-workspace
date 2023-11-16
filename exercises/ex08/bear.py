"""File to define Bear class."""


class Bear:
    """The bear class."""
    age: int
    hunger_score: int
    
    def __init__(self):
        """Constructes the Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """One day in the bears life."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bears eating."""
        self.hunger_score += num_fish