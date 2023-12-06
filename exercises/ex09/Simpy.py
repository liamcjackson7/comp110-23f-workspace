"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730665100"


class Simpy:
    """Defines everything that makes up the Simpy class."""
    values: list[float]
    
    def __init__(self, values: list[float]):
        """Constructor."""
        self.values = values
    
    def __str__(self) -> str:
        """String magic method."""
        return f"Simpy({self.values})"
    
    def fill(self, fill_float: float, fill_int: int) -> None:
        """Fills self.values."""
        self.values = [fill_float] * fill_int
        
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Aranges the values in self.value."""
        assert step != 0.0, "Step cannot be 0.0"
        num_values = int((stop - start) / step)
        self.values = [start + i * step for i in range(num_values)]
            
    def sum(self) -> float:
        """Adds all of the self.values together."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """The __add__ magic method."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            new_values = [self.values[i] + rhs.values[i] for i in range(len(self.values))]
        else:
            new_values = [self.values[i] + rhs for i in range(len(self.values))]
        return Simpy(new_values)
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """The __pow__ magic method."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            new_values = [self.values[i] ** rhs.values[i] for i in range(len(self.values))]
        else:
            new_values = [self.values[i] ** rhs for i in range(len(self.values))]
        return Simpy(new_values)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """The __eq__ magic method."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            return [self.values[i] == rhs.values[i] for i in range(len(self.values))]
        else:
            return [self.values[i] == rhs for i in range(len(self.values))]
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """The __gt__ magic method."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            return [self.values[i] > rhs.values[i] for i in range(len(self.values))]
        else:
            return [self.values[i] > rhs for i in range(len(self.values))]
        
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """The __getitem__ magic method."""
        if isinstance(rhs, int):
            return self.values[rhs]
        elif isinstance(rhs, list) and all(isinstance(item, bool) for item in rhs):
            result_values = [value for value, mask in zip(self.values, rhs) if mask]
            return Simpy(result_values)
        else:
            raise TypeError("Unsupported index type")
        
