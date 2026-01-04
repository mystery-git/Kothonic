class Triple:
	def __init__(self, first: object, second: object, third: object) -> None:
		self.first = first
		self.second = second
		self.third = third

	def __call__(self) -> tuple[object, object, object]:
		return self.first, self.second, self.third

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, Triple):
			return False
		return self.first == other.first and self.second == other.second and self.third == other.third
