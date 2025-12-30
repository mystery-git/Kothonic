from typing import Generic
from typing import TypeVar
from typing import Any

T = TypeVar("T")

class KotlinValue(Generic[T]):
	value: T

	def elvis(self, other: Any) -> Any:
		return self.value or other
