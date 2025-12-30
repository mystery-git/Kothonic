from typing import (
    Callable,
    Optional,
    TypeVar,
)

from forbiddenfruit import curse  # type: ignore

T = TypeVar("T")


def _is_builtin(obj):
    return type(obj).__module__ == "builtins"


def inject_func_into(classes: list[object], func: Callable, name: Optional[str] = None):
    name = name or func.__name__

    for cls in classes:
        if _is_builtin(cls):
            curse(cls, name, func)
        else:
            setattr(cls, name, func)
