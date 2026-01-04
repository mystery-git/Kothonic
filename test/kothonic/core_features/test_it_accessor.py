import pytest

from kothonic.core_features.it_accessor import it


class ChainedObject:
	def __init__(self, val):
		self.val = val

	def method(self):
		return self.val

	def next(self):
		return ChainedObject(self.val + "_next")

	def add(self, suffix):
		return self.val + suffix


class TestItAccessor:
	"""Tests for the ItAccessor ('it') utility."""

	def test_identity(self):
		"""Test 'it' as an identity function."""
		assert it("test") == "test"

	def test_simple_method_call(self):
		"""Test calling a method on the target object."""
		# Equivalent to lambda x: x.upper()
		func = it.upper()
		assert func("hello") == "HELLO"

	def test_chained_method_calls(self):
		"""Test verifying deeply nested attribute/method access."""
		# Equivalent to lambda x: x.next().method()
		chain_func = it.next().method()
		obj = ChainedObject("start")

		# obj.next() -> ChainedObject("start_next")
		# .method() -> "start_next"
		assert chain_func(obj) == "start_next"

	def test_method_with_args(self):
		"""Test calling methods with arguments in the chain."""
		# Equivalent to lambda x: x.add("_end")
		func = it.add("_end")
		obj = ChainedObject("start")
		assert func(obj) == "start_end"

	def test_map_usage_context(self):
		"""CRITICAL: Test usage in map/filter contexts."""
		data = ["a", "b", "c"]
		# using it.upper() in map
		result = list(map(it.upper(), data))
		assert result == ["A", "B", "C"]

	def test_scope_behavior(self):
		"""Test behavior within local scopes and closures."""

		def local_transformer():
			# Define 'it' usage locally
			transformer = it.upper()
			return transformer("scoped")

		assert local_transformer() == "SCOPED"

		# Verify it works inside a context manager (simulating scope)
		with pytest.raises(ValueError, match="ScopeCheck"):
			f = it.lower()
			if f("TEST") == "test":
				raise ValueError("ScopeCheck")
