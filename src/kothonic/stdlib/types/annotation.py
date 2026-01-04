from collections.abc import Callable


# TODO("PAUSED")
# TODO("CURRENTLY DOESNT DO EVERYTHING ANNOTATION IN KOTLIN DOES")
def Annotation(*args, **kwargs):  # noqa: N802
	def decorator(obj: Callable):
		if not hasattr(obj, "__metadata__"):
			setattr(obj, "__metadata__", [])

		obj.__metadata__.append([*args, *kwargs])  # type: ignore

		def wrapper(*args, **kwargs):
			return obj(*args, **kwargs)

		return wrapper

	return decorator
