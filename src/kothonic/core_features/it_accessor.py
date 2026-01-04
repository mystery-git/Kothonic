class ItAccessor:
	"""
	A helper class to create deferred callable chains, similar to Kotlin's 'it' in lambdas,
	but adapted for Python's syntax.
	Usage: `map(it.upper(), ["a", "b"])`
	"""

	def __init__(self, action=None):
		self.action = action if action else (lambda x: x)

	def __getattr__(self, name):
		"""
		Support for method chaining.
		Returns a function that, when called with args, returns a new ItAccessor
		that applies the method 'name' with those args to the result of the previous action.

		Note: This assumes 'name' refers to a method or callable attribute on the target object.
		Usage: it.method_name(args)
		"""

		def _deferred_method(*args, **kwargs):
			def new_action(x):
				return getattr(self.action(x), name)(*args, **kwargs)

			return ItAccessor(new_action)

		return _deferred_method

	def __call__(self, value):
		"""Executes the accumulated action on the given value."""
		return self.action(value)
		return self.action(value)


it = ItAccessor()
