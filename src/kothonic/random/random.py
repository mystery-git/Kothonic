import sys
import random

from ..stdlib import Int


class Random:
	def __init__(self, seed: int | Int):
		self.__seed = seed

	@staticmethod
	def next_int() -> int | Int:
		return random.randint(0, sys.maxsize)
