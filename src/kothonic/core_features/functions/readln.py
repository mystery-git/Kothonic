from kothonic.stdlib.types.string import String


def readln(target) -> String:
	return String(input(f"\n{target}"))
