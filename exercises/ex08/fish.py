"""File to define Fish class."""


class Fish:
    """Fish class."""
    age: int

    def __init__(self):
        """Constructs the fish class."""
        self.age = 0
        return None
    
    def one_day(self):
        """One day in the life of the fish."""
        self.age += 1
        return None