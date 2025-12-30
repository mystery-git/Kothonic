from typing import Callable

from forbiddenfruit import curse  # type: ignore


def __is_builtin(obj):
    return type(obj).__module__ == "builtins"

def extension(self: object):
    def decorator(func: Callable):
        if hasattr(self, func.__name__):
            raise Exception(f"{self.__class__.__name__} already has an attribute named {func.__name__}")
    
        if __is_builtin(self):
            curse(self, func.__name__, func)
        else:
            setattr(self, func.__name__, func)

        return func

    return decorator