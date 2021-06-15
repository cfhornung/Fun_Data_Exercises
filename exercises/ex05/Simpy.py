"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "720053793"


class Simpy:
    """My class."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        """Initialize."""
        self.values = values

    def __repr__(self) -> str:
        """Prints into a string."""
        return f"Simpy({self.values})"

    def fill(self, x: float, y: int) -> None:
        """Fill Simpy's values with repeating values."""
        numbers: list[float] = []
        while len(numbers) < y:
            numbers.append(x)
        self.values = numbers

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Range function."""
        assert step != 0.0
        results: list[float] = []
        if start < stop:
            while start < stop:
                results.append(start)
                start += step
        else:
            while start > stop:
                results.append(start)
                start += step
        self.values = results

    def sum(self) -> float:
        """Sums values."""
        total = sum(self.values)
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds values."""
        results: list[float] = []
        values = self.values
        if isinstance(rhs, Simpy):
            assert len(values) == len(rhs.values)
            for i in range(len(values)):
                results.append(values[i] + rhs.values[i])
        else:
            for i in values:
                results.append(i + rhs)
        return Simpy(results)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raises values to a power."""
        results: list[float] = []
        values = self.values
        if isinstance(rhs, Simpy):
            assert len(values) == len(rhs.values)
            for i in range(len(values)):
                results.append(values[i] ** rhs.values[i])
        else:
            for i in values:
                results.append(i ** rhs)
        return Simpy(results)

    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Remainders."""
        results: list[float] = []
        values = self.values
        if isinstance(rhs, Simpy):
            assert len(values) == len(rhs.values)
            for i in range(len(values)):
                results.append(values[i] % rhs.values[i])
        else:
            for i in values:
                results.append(i % rhs)
        return Simpy(results)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Makes a mask of booleans."""
        mask: list[bool] = []
        values = self.values
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(values)):
                mask.append(values[i] == rhs.values[i])
        else:
            for i in values:
                mask.append(i == rhs)
        return mask

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """List of booleans."""
        mask: list[bool] = []
        values = self.values
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(values)):
                mask.append(values[i] > rhs.values[i])
        else:
            for i in values:
                mask.append(i > rhs)
        return mask

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Access items via an index."""
        results: list[float] = []
        values = self.values
        if isinstance(rhs, int):
            return values[rhs]
        else:
            assert len(values) == len(rhs)
            for i in range(len(rhs)):
                if rhs[i]:
                    results.append(values[i])
        return Simpy(results)