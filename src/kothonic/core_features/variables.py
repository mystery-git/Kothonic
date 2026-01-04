from typing import TypeVar

from .inline_value import InlineValue
from .kotlin_value import KotlinValue


T = TypeVar("T")


class var(InlineValue[T], KotlinValue[T]):  # noqa: N801
	pass


class val(InlineValue[T], KotlinValue[T]):  # noqa: N801
	pass
