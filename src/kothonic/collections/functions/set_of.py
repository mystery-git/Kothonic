from typing import TypeVar
from collections.abc import Iterable

from ..types.set import Set


T = TypeVar("T")


# Kotlin: fun <T> setOf(vararg elements: T): Set[T]
def set_of(items: Iterable[T] = ()) -> Set[T]:
	return Set(items)
