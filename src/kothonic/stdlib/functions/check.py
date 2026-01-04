from collections.abc import Callable

from ..exceptions.illegal_state_exception import IllegalStateException


def check(value: bool, lazy_message: str | Callable[[], str] | None = None) -> None:
	if not value:
		if lazy_message:
			message = lazy_message() if callable(lazy_message) else lazy_message
			raise IllegalStateException(message)
		raise IllegalStateException
