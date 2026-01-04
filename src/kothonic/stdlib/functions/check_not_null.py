from typing import TypeVar, overload
from collections.abc import Callable

from ..exceptions.illegal_state_exception import IllegalStateException


T = TypeVar("T")


@overload
def check_not_null(value: T | None, lazy_message: str | Callable[[], str]) -> T: ...


@overload
def check_not_null(value: T | None) -> T: ...


def check_not_null(value: T | None, lazy_message: str | Callable[[], str] | None = None) -> T:
	if value is None:
		if lazy_message is None:
			raise IllegalStateException
		message = lazy_message() if callable(lazy_message) else lazy_message
		raise IllegalStateException(message)
	return value
