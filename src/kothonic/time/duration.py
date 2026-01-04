from datetime import timedelta


class Duration(timedelta):
	__SECONDS_IN_DAY = 86400
	__SECONDS_IN_HOUR = 3600
	__SECONDS_IN_MIN = 60

	def in_whole_days(self) -> int:
		return round(self.total_seconds() / self.__SECONDS_IN_DAY)

	def in_whole_hours(self) -> int:
		return round(self.total_seconds() / self.__SECONDS_IN_HOUR)

	def in_whole_minutes(self) -> int:
		return round(self.total_seconds() / self.__SECONDS_IN_MIN)

	def in_whole_seconds(self) -> int:
		return round(self.total_seconds())
