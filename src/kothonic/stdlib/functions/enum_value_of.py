from typing import TypeVar

from ..types.enum_class.enum import Enum


T = TypeVar("T", bound=Enum)


def enum_value_of(cls: type[T], name: str) -> T:
	return cls.value_of(name)
