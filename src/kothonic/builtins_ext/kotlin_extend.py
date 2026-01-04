from kothonic.utils import inject_func_into

from .int_ext import cursable_funcs as int_funcs
from .map_ext import cursable_funcs as map_funcs
from .set_ext import cursable_funcs as set_funcs
from .str_ext import cursable_funcs as str_funcs
from .list_ext import cursable_funcs as list_funcs
from .float_ext import cursable_funcs as float_funcs


# Map types to their respective extension functions
_EXTENSIONS = {
	str: (str, str_funcs),
	int: (int, int_funcs),
	float: (float, float_funcs),
	list: (list, list_funcs),
	set: (set, set_funcs),
	dict: (dict, map_funcs),
}


def kotlin_extend(t: type) -> None:
	"""Use this function to extend the builtins types such as str or int with Kotlin-like "extensions"."""
	if t not in _EXTENSIONS:
		raise ValueError(f"Invalid type: {t}")

	target_type, funcs = _EXTENSIONS[t]
	for func in funcs:
		inject_func_into(target_type, func)
