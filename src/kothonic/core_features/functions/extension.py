from types import FunctionType


def extension(self: object):
	"""Special decorator to add a new method to a class."""

	def decorator(func: FunctionType):
		func_name = getattr(func, "__name__")

		if hasattr(self, func_name):
			raise Exception(f"{self.__class__.__name__} already has an attribute named {func_name}")

		setattr(self, func_name, func)

		return func

	return decorator
