from typing import TypeVar
from collections.abc import Callable


T = TypeVar("T")
R = TypeVar("R")


def apply(self: T, func: Callable[[T], R]) -> R:
	return func(self)
