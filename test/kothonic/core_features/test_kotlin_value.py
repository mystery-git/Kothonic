from kothonic.core_features.kotlin_value import KotlinValue


class MockValue(KotlinValue[str]):
	def __init__(self, val):
		self._val = val

	@property
	def _kotlin_value(self) -> str:
		"""Helper to return the stored value."""
		return self._val


class TestKotlinValue:
	"""Tests for the KotlinValue base class."""

	def test_elvis_operator(self):
		"""
		Test the elvis method (?:).
		Should return the value if truthy, else the default.
		"""
		a = MockValue("value")
		b = MockValue(None)
		c = MockValue("")  # Empty string is falsy in Python

		assert a.elvis("default") == "value"
		assert b.elvis("default") == "default"
		# Kotlin's elvis usually checks for nullity, but here implementation uses `or`
		# which checks truthiness.
		# If the implementation is `return self._kotlin_value or other`, existing python behavior is truthiness.
		# If strict null check is desired, implementation should be `val if val is not None else other`.
		# Based on current implementation (and likely pythonic intent), empty string -> default.
		assert c.elvis("default") == "default"

	def test_to_string(self):
		"""Test the to_string method returning a kothonic String."""
		a = MockValue("test_str")
		# to_string imports String internally, so we don't strictly need it at module level
		# unless we want to isinstance check, but checking str() is sufficient for value.
		result = a.to_string()
		assert str(result) == "test_str"
		assert type(result).__name__ == "String"
