from typing import Generic, TypeVar


T = TypeVar("T")
U = TypeVar("U")


class Pair(Generic[T, U]):
	def __init__(self, first: T, second: U) -> None:
		self.first: T = first
		self.second: U = second

	def __call__(self) -> tuple[T, U]:
		return self.first, self.second

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, Pair):
			return False
		return self.first == other.first and self.second == other.second
