from typing import TypeVar
from .kotlin_value import KotlinValue
from .value_class import InlineValue

T = TypeVar("T")

class var(KotlinValue[T], InlineValue[T]):
		pass

class val(KotlinValue[T], InlineValue[T]):
		pass
