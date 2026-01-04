from kothonic.stdlib import String
from kothonic.core_features.kotlin_value import KotlinValue


cursable_funcs = [
	String.to_int,
	String.to_int_or_null,
	String.to_float,
	KotlinValue.let,
	KotlinValue.apply,
	String.to_float_or_null,
	String.is_null_or_empty,
	String.is_null_or_blank,
	String.reversed_,
	String.uppercase,
	String.lowercase,
	String.trim,
	String.trim_start,
	String.trim_end,
	String.substring,
	String.contains,
	String.starts_with,
	String.ends_with,
	String.capitalize_,
	String.take,
	String.take_last,
	String.drop,
	String.drop_last,
	String.index_of,
	String.is_digit,
	String.to_list,
	String.plus,
	String.reversed_,
]
