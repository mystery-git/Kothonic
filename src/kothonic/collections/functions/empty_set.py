from typing import TypeVar

from ..types.set import Set


T = TypeVar("T")


def empty_set() -> Set[T]:
	return Set()
