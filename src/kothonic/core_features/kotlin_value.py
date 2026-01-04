from __future__ import annotations

from typing import TYPE_CHECKING, Any, Self, Generic, TypeVar
from collections.abc import Callable


if TYPE_CHECKING:
	from kothonic.stdlib import String

T = TypeVar("T")


class KotlinValue(Generic[T]):
	@property
	def _kotlin_value(self) -> T:
		"""
		Returns the underlying Kotlin value wrapped by this object.
		Must be implemented by subclasses.
		"""
		raise NotImplementedError

	def to_string(self) -> String:
		"""
		Returns a String representation of the object, similar to Kotlin's toString().
		wraps the python str() result in a kothonic String.
		"""
		from kothonic.stdlib import String

		val = getattr(self, "_kotlin_value", self)
		return String(str(val))

	def elvis(self, other: Any) -> Any:
		"""
		Implements the Elvis operator (?:) logic.
		Returns the inner value if it is truthy, otherwise returns 'other'.
		"""
		return self._kotlin_value or other

	def let(self, block: Callable[[T], Any]) -> Any:
		"""
		Calls the specified function [block] with `this` value as its argument and returns its result.
		"""
		return block(self._kotlin_value)

	def apply(self, block: Callable[[Self], Any]) -> Self:
		"""
		Calls the specified function [block] with `this` value as its argument and returns `this` value.
		"""
		block(self)
		return self
