from collections.abc import Callable


def assert_(value: bool, lazy_message: str | Callable[..., str] | None = None) -> None:
	if not value:
		if lazy_message:
			message = lazy_message() if callable(lazy_message) else lazy_message
			raise AssertionError(message)
		raise AssertionError
