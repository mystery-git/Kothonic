import pytest  # noqa

from kothonic.stdlib import Float


float_val: float = 123.456
int_val: int = 123
test_float: Float = Float(float_val)


def test_kt_float():
	assert isinstance(test_float, Float)
	assert isinstance(test_float, float)


def test_to_int():
	assert test_float.to_int() == int_val
	assert isinstance(test_float.to_int(), int)

	# Test truncation/rounding behavior
	assert Float(5.9).to_int() == 5
	assert Float(5.1).to_int() == 5
	assert Float(-5.9).to_int() == -5

	# Test edge cases (NaN, Infinity)
	with pytest.raises(ValueError):
		Float(float("nan")).to_int()

	with pytest.raises(OverflowError):
		Float(float("inf")).to_int()

	with pytest.raises(OverflowError):
		Float(float("-inf")).to_int()


def test_to_int_or_null():
	as_an_int = test_float.to_int()
	assert as_an_int == int_val
	assert isinstance(as_an_int, int)

	assert Float(100.1).to_int_or_null() == 100

	# Test edge cases (NaN, Infinity)
	assert Float(float("nan")).to_int_or_null() is None
	assert Float(float("inf")).to_int_or_null() is None
	assert Float(float("-inf")).to_int_or_null() is None


def test_to_string():
	assert test_float.to_string() == "123.456"
	assert isinstance(test_float.to_string(), str)


if __name__ == "__main__":
	pytest.main([__file__])
