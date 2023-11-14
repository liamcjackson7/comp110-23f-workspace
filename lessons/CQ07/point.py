"""Challenge Question Class."""
from __future__ import annotations
 
 
class Point:
    """Class to represent (x,y) coordinate point."""
    
    x: float
    y: float
    
    def __init__(self, x: float = 0, y: float = 0):
        """Instance variables."""
        self.x = x
        self.y = y

    def __str__(self):
        """Makes the points readable."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Modify (or mutate) a point."""
        return Point(self.x * factor, self.y * factor)
        
    def __add__(self, factor: int | float) -> Point:
        """Make a new point."""
        return Point(self.x + factor, self.y + factor)
