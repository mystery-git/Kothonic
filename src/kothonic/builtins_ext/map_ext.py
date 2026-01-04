from kothonic.collections import Map
from kothonic.core_features.kotlin_value import KotlinValue


cursable_funcs = [
	Map.contains_key,
	Map.contains_value,
	Map.filter_,
	KotlinValue.let,
	KotlinValue.apply,
	Map.filter_keys,
	Map.filter_values,
	Map.map_,
	Map.plus,
	Map.all_,
	Map.any_,
	Map.associate,
	Map.average,
	Map.contains,
	Map.contains_all,
	Map.count_,
	Map.distinct,
	Map.drop,
	Map.drop_last,
	Map.element_at,
	Map.element_at_or_null,
	Map.element_at_or_else,
	Map.find,
	Map.first,
	Map.first_not_null,
	Map.first_or_null,
	Map.size,
	Map.entries,
]
