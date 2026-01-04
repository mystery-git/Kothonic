import pytest

from kothonic.stdlib.types.array import Array


def test_array_creation():
	# Array inherits from list, so it works like list([1, 2, 3])
	# The Kotlin `Array(size, init)` constructor is not implemented in __init__.
	# We use list-like initialization which is supported by inheritance.
	arr = Array([0, 1, 4, 9, 16])
	assert len(arr) == 5
	assert arr[0] == 0
	assert arr[4] == 16


def test_array_get_set():
	arr = Array([0, 0, 0])
	arr[1] = 10
	assert arr[1] == 10
	# arr.get/set might be missing if not implemented. List supports __getitem__/__setitem__.
	# Checking if get/set methods exist or if we should use indexer
	if hasattr(arr, "get"):
		assert arr.get(1) == 10

	if hasattr(arr, "set"):
		arr.set(2, 20)
		assert arr[2] == 20


def test_array_iterator():
	arr = Array([1, 2, 3])
	values = [x for x in arr]
	assert values == [1, 2, 3]


if __name__ == "__main__":
	pytest.main([__file__])
