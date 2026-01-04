from typing import Generic, TypeVar
from dataclasses import dataclass


T = TypeVar("T")


@dataclass
class IndexedValue(Generic[T]):
	index: int
	value: T
