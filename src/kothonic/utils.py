from functools import singledispatch
from collections.abc import Callable

from forbiddenfruit import curse


def _is_builtin(obj):
	return type(obj).__module__ == "builtins"


@singledispatch
def inject_func_into(classes: list[object], func: Callable, name: str | None = None) -> None:
	if name is None:
		if isinstance(func, property):
			name = func.__name__
		else:
			name = getattr(func, "__name__")

	for cls in classes:
		if _is_builtin(cls):
			curse(cls, name, func)
		else:
			setattr(cls, name, func)


@inject_func_into.register
def _(cls: object, func: Callable, name: str | None = None) -> None:
	if name is None:
		if isinstance(func, property):
			name = func.__name__
		else:
			name = getattr(func, "__name__")

	if _is_builtin(cls):
		curse(cls, name, func)
	else:
		setattr(cls, name, func)
