import pytest

from kothonic.core_features.inline_value import InlineValue


class TestInlineValue:
	"""Tests for the InlineValue proxy wrapper."""

	def test_wrapping_and_unwrapping(self):
		"""Test basic wrapping and _kotlin_value access."""
		val = 123
		wrapped = InlineValue(val)
		assert wrapped.value == val
		assert wrapped._kotlin_value == val
		assert wrapped == 123  # Should equal the raw value due to proxying

	def test_proxy_attributes(self):
		"""Test proxying of attribute access."""
		val = "hello"
		wrapped = InlineValue(val)
		# "hello" has .upper()
		assert wrapped.upper() == "HELLO"

	def test_proxy_dunder_methods(self):
		"""Test proxying of common dunder methods (len, getitem, etc)."""
		val = [1, 2, 3]
		wrapped = InlineValue(val)

		# __len__
		assert len(wrapped) == 3
		# __getitem__
		assert wrapped[0] == 1
		# __setitem__
		wrapped[0] = 10
		assert val[0] == 10
		# __contains__
		assert 10 in wrapped

	def test_arithmetic_ops(self):
		"""Test arithmetic operations proxying."""
		a = InlineValue(5)
		b = InlineValue(10)

		# Add
		assert a + b == 15
		assert a + 5 == 10
		assert 5 + a == 10

		# Sub
		assert b - a == 5

		# Mul
		assert a * 2 == 10

		# Div
		assert b / a == 2.0

		# In-place ops (should modify value)
		a += 1
		assert a.value == 6

	def test_comparison_ops(self):
		"""Test comparison operators."""
		val1 = InlineValue(10)
		val2 = InlineValue(20)

		assert val1 < val2
		assert val2 > val1
		assert val1 != val2
		assert val1 == 10

	def test_type_conversions(self):
		"""Test int(), float(), bool(), str() conversions."""
		val = InlineValue(5)
		assert str(val) == "5"
		assert int(val) == 5
		assert float(val) == 5.0
		assert bool(val) is True

		zero = InlineValue(0)
		assert bool(zero) is False

	def test_setattr_restriction(self):
		"""Test that setting attributes other than 'value' is restricted."""
		wrapped = InlineValue("test")

		# Should be able to set 'value'
		wrapped.value = "new"
		assert wrapped.value == "new"

		# Should NOT be able to set arbitrary attributes on the wrapper itself
		# because of __slots__ and __setattr__ logic
		with pytest.raises(AttributeError):
			wrapped.new_attr = "fail"
