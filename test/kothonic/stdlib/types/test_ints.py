import pytest  # noqa

from kothonic.stdlib import Int


int_val: int = 123
float_val: float = 123.0
test_int: Int = Int(int_val)


def test_kt_int():
	assert isinstance(test_int, Int)
	assert isinstance(test_int, int)


def test_to_float():
	as_a_float = test_int.to_float()
	assert as_a_float == float_val
	assert isinstance(as_a_float, float)


def test_to_float_or_null():
	assert test_int.to_float_or_null() == float_val
	assert isinstance(test_int.to_float_or_null(), float)


def test_to_string():
	assert test_int.to_string() == "123"
	assert isinstance(test_int.to_string(), str)


if __name__ == "__main__":
	pytest.main([__file__])
