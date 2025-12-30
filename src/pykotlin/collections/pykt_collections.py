from typing import (
    Callable,
    Collection,
    Dict,
    Iterable,
    List,
    Tuple,
    TypeVar,
    Union,
)

K = TypeVar("K")
V = TypeVar("V")
T = TypeVar("T")
R = TypeVar("R")


# Kotlin: fun <T> Iterable<T>.filter(predicate: (T) -> Boolean): List<T>
def filter_(self: Iterable[T], predicate: Callable[[T], bool]) -> List[T]:
    """Returns a list containing only elements matching the given predicate."""

    return list(filter(predicate, self))


# Kotlin: fun <T, R> Iterable<T>.map(transform: (T) -> R): List<R>
def map_(self: Iterable[T], transformation: Callable[[T], R]) -> List[R]:
    """Returns a list containing the results of applying the given transform function to each element in the original collection."""

    return list(map(transformation, self))


# Kotlin: operator fun <T> Collection<T>.plus(elements: Iterable<T>): List<T>
def plus(self: Collection[T], elements: Collection[T]) -> List[T]:
    """Returns a list containing all elements of the original collection and then all elements of the given elements."""
    return list(self) + list(elements)


# Kotlin: fun <T> Iterable<T>.all(predicate: (T) -> Boolean): Boolean
def all_(self: Iterable[T], predicate: Callable[[T], bool]) -> bool:
    """Returns true if all elements match the given predicate."""
    return all(predicate(item) for item in self)


# Kotlin: fun <T> Iterable<T>.any(predicate: (T) -> Boolean): Boolean
def any_(self: Iterable[T], predicate: Callable[[T], bool]) -> bool:
    """Returns true if at least one element matches the given predicate."""
    return any(predicate(item) for item in self)


# Kotlin: fun <T, K, V> Iterable<T>.associate(transform: (T) -> Pair<K, V>): Map<K, V>
def associate(self: Iterable[T], transform: Callable[[T], Tuple[K, V]]) -> Dict[K, V]:
    """Returns a Map containing key-value pairs provided by transform function applied to elements of the given collection."""
    # TODO("Logic bug: 'by' is the function itself, not the result of by(item)")

    new_dict = {}

    for item in self:
        key, value = transform(item)
        new_dict[key] = value

    return new_dict


# Kotlin: fun Iterable<Number>.average(): Double
def average(self: Iterable[Union[int, float]]) -> float:
    """Returns an average value of elements in the collection."""
    items = list(self)
    return sum(items) / len(items)


# Kotlin: operator fun <T> Collection<T>.contains(element: T): Boolean
def contains(self: Collection[T], element: T) -> bool:
    """Returns true if the element is found in the collection."""
    return element in self


# Kotlin: fun <T> Collection<T>.containsAll(elements: Collection<T>): Boolean
def contains_all(self: Collection[T], elements: Collection[T]) -> bool:
    """Checks if all elements in the specified collection are contained in this collection."""

    container = list(self)
    return all(element in container for element in elements)


# Kotlin: fun <T> Collection<T>.count(): Int
def count_(self: Collection[T]) -> int:
    """Returns the number of elements in this collection."""
    return len(list(self))


# Kotlin: fun <T> Iterable<T>.distinct(): List<T>
def distinct(self: Iterable[T]) -> List[T]:
    """Returns a collection containing only distinct elements from the given collection."""
    return list(set(self))


# Kotlin: fun <T> Iterable<T>.drop(n: Int): List<T>
def drop(self: Iterable[T], n: int) -> List[T]:
    """Returns a list containing all elements except first n elements."""
    return list(self)[n:]


# Kotlin: fun <T> List<T>.dropLast(n: Int): List<T>
def drop_last(self: List[T], n: int) -> List[T]:
    """Returns a list containing all elements except last n elements."""
    items = list(self)
    return items[: len(items) - n]


# Kotlin: fun <T> Iterable<T>.elementAt(index: Int): T
def element_at(self: Iterable[T], index: int) -> T:
    """Returns an element at the given index or throws an exception if the index is out of bounds of this collection."""
    return list(self)[index]


# Kotlin: fun <T> Iterable<T>.elementAtOrNull(index: Int): T?
def element_at_or_null(self: Iterable[T], index: int) -> Union[T, None]:
    """Returns an element at the given index or null if the index is out of bounds of this collection."""
    try:
        return list(self)[index]
    except IndexError:
        return None


# Kotlin: fun <T> Iterable<T>.elementAtOrElse(index: Int, defaultValue: (Int) -> T): T
def element_at_or_else(
    self: Iterable[T], index: int, defaultValue: Callable[[int], T]
) -> T:
    """Returns an element at the given index or the result of calling the defaultValue function if the index is out of bounds."""

    try:
        return list(self)[index]
    except IndexError:
        return defaultValue(index)


# Kotlin: fun <T> Iterable<T>.find(predicate: (T) -> Boolean): T?
def find(self: Iterable[T], predicate: Callable[[T], bool]) -> Union[T, None]:
    """Returns the first element matching the given predicate, or null if no such element was found."""

    for element in self:
        if predicate(element):
            return element
    return None


# Kotlin: fun <T> Iterable<T>.first(): T
def first(self: Iterable[T]) -> T:
    """Returns the first element."""
    return list(self)[0]


# Kotlin: Custom: Returns first non-null element
def first_not_null(self: Iterable[T]) -> Union[T, None]:
    """Returns the first element that is not null."""

    for element in self:
        if element is not None:
            return element
    return None


# Kotlin: fun <T> Iterable<T>.firstOrNull(): T?
def first_or_null(self: Iterable[T]) -> Union[T, None]:
    """Returns the first element, or null if the collection is empty."""
    return next(iter(self), None)
