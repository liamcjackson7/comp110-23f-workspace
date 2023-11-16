"""File to define River class."""

__author__ = "730665100"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Defines the River class."""
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

    def check_ages(self):
        """Checks and removes the ages of the animals."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bears for bears in self.bears if bears.age <= 5]
        return None
    
    def remove_fish(self, amount: int):
        """Removes the fish from the river."""
        self.fish = self.fish[amount:]
        return None

    def bears_eating(self):
        """Bears eating the fish and removing the fish."""
        for bears in self.bears:
            if (len(self.fish)) >= 5:
                bears.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checks the hunger of the bears."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        return None
        
    def repopulate_bears(self):
        """Repopulates the fish in the river."""
        num_bear_pairs = len(self.bears) // 2
        self.bears += [Bear() for i in range(num_bear_pairs)]
        return None
    
    def repopulate_fish(self):
        """Repopulates the bears population."""
        num_fish_pairs = len(self.fish) // 2
        self.fish += [Fish() for i in range(num_fish_pairs * 4)]
        return None
    
    def view_river(self):
        """Prints the stats of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
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
        """Simulates one week in the river."""
        for _ in range(7):
            self.one_river_day()
            
