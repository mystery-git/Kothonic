from dataclasses import dataclass

import pytest

from kothonic import String, KotlinValue


def test_apply_returns_self():
	# Verify apply returns the receiver (identity check)
	s = String("hello")
	res = s.apply(lambda x: None)
	assert res is s
	assert res == "hello"


def test_on_dataclass():
	@dataclass
	class MyClass(KotlinValue):
		x: int

	my_class = MyClass(1)
	assert my_class.x == 1
	my_class.x = 2
	assert my_class.x == 2
	my_class.apply(lambda it: print(it.x))
	assert my_class.x == 2


if __name__ == "__main__":
	pytest.main([__file__])
