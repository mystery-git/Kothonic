import pytest  # noqa: F401

from kothonic.core_features import val, var


def test_kot_variables_val():
	a = 5
	b = 10
	c = None

	z = val(a).elvis(6)

	assert z == a

	y = val(b).elvis(11)

	assert y == b

	x = val(c).elvis(5)

	assert x == 5

	n = val(5)

	assert isinstance(n, val)

	n += 4

	assert isinstance(n, val)

	assert n == 9


def test_kot_variables_var():
	v = var(10)
	assert v == 10
	assert v.value == 10

	# var should allow changing value
	v.value = 20  # type: ignore
	assert v == 20
	assert v.value == 20

	# Math operations
	v += 5
	assert v == 25
	assert isinstance(v, var)

	v = v - 10
	assert v == 15
	assert isinstance(v, var)

	# Elvis operator
	v_null = var(None)
	assert v_null.elvis(100) == 100


def test_val_vs_var_behavior():
	# Currently val and var behave similarly at runtime in terms of mutation

	# because they both inherit from InlineValue which allows setting .value

	# This test ensures they both satisfy the InlineValue interface.

	v1 = val(1)

	v2 = var(2)

	assert v1 + v2 == 3

	assert isinstance(v1 + v2, val)  # val + var -> val because val is first

	assert v2 + v1 == 3

	assert isinstance(v2 + v1, var)  # var + val -> var because var is first


def test_val_var_type_hints():
	def process_val(v: val[int]) -> int:
		return v.value * 2

	def process_var(v: var[int]) -> int:
		return v.value * 2

	assert process_val(val(10)) == 20
	assert process_var(var(10)) == 20


def test_val_with_mutable_literals():
	# val protects re-assignment, but if content is mutable, it can change
	list_val = val([1, 2, 3])
	list_val.append(4)
	assert list_val == [1, 2, 3, 4]
	assert list_val[0] == 1


def test_var_with_literals():
	v = var({"key": "value"})
	assert v["key"] == "value"

	v.value = {"key": "new value"}
	assert v["key"] == "new value"


def test_wrapped_object_behavior():
	s = val("hello")

	try:
		assert s.startswith("h")
	except Exception as e:
		raise e

	# Check list methods
	lst = var([1, 2])
	lst.append(3)
	assert len(lst) == 3


if __name__ == "__main__":
	pytest.main([__file__])
