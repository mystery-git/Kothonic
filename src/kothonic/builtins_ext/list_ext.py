from kothonic.collections import List
from kothonic.core_features.kotlin_value import KotlinValue


cursable_funcs = [
	List.filter_,
	List.map_,
	List.plus,
	List.all_,
	List.any_,
	List.associate,
	List.average,
	List.contains,
	List.contains_all,
	List.distinct,
	List.drop,
	List.drop_last,
	List.element_at,
	List.element_at_or_null,
	List.element_at_or_else,
	List.find,
	List.first,
	List.first_not_null,
	List.first_or_null,
	List.flatten,
	List.count_,
	List.size,
	List.is_empty,
	List.is_not_empty,
	KotlinValue.let,
	KotlinValue.apply,
]
