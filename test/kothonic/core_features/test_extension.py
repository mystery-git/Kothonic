import pytest

from kothonic import extension


def test_basic_extension():
	class MyClass:
		pass  # No methods

	@extension(MyClass)
	def my_extension(self):
		return "extension"

	assert MyClass().my_extension() == "extension"  # type: ignore


def test_extension_with_args():
	class MyClass:
		def __init__(self, x: int, y: int):
			self.x = x
			self.y = y

		def __eq__(self, other):
			if not isinstance(other, MyClass):
				return NotImplemented
			return self.x == other.x and self.y == other.y

	@extension(MyClass)
	def add(self, other: "MyClass") -> "MyClass":  # type: ignore
		return MyClass(self.x + other.x, self.y + other.y)

	assert MyClass(1, 2).add(MyClass(3, 4)) == MyClass(4, 6)  # type: ignore


if __name__ == "__main__":
	pytest.main([__file__])
