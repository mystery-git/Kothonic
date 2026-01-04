from kothonic.collections import Set
from kothonic.core_features.kotlin_value import KotlinValue


cursable_funcs = [
	Set.filter_,
	Set.map_,
	Set.plus,
	Set.all_,
	Set.any_,
	Set.associate,
	Set.average,
	Set.contains,
	Set.contains_all,
	Set.count_,
	Set.distinct,
	Set.drop,
	Set.drop_last,
	Set.element_at,
	Set.element_at_or_null,
	Set.element_at_or_else,
	Set.find,
	Set.first,
	Set.first_not_null,
	Set.first_or_null,
	Set.size,
	Set.is_empty,
	Set.is_not_empty,
	KotlinValue.let,
	KotlinValue.apply,
]
