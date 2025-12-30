import builtins
from typing import Any, Callable, Collection, TypeAlias, Union
from typing import Dict as _Dict
from typing import List as _List

class kt_map(builtins.dict):
    def contains_key(self, key: Any) -> builtins.bool:
        """Returns true if the map contains the specified key."""
        ...

    def contains_value(self, value: Any) -> builtins.bool:
        """Returns true if the map maps one or more keys to the specified value."""
        ...

    def filter_(self, predicate: Callable[[Any], bool]) -> _List[Any]:
        """Returns a list containing only elements matching the given predicate."""
        ...

    def map_(self, transformation: Callable[[Any], Any]) -> _List[Any]:
        """Returns a list containing the results of applying the given transform function to each element in the original collection."""
        ...

    def all_(self, predicate: Callable[[Any], bool]) -> builtins.bool:
        """Returns true if all elements match the given predicate."""
        ...

    def any_(self, predicate: Callable[[Any], bool]) -> builtins.bool:
        """Returns true if at least one element matches the given predicate."""
        ...

    def associate(
        self, transform: Callable[[Any], builtins.tuple[Any, Any]]
    ) -> builtins.dict[Any, Any]:
        """Returns a Map containing key-value pairs provided by transform function applied to elements of the given collection."""
        ...

    def average(self) -> builtins.float:
        """Returns an average value of elements in the collection."""
        ...

    def contains(self, match: Any) -> builtins.bool:
        """Returns true if the element is found in the collection."""
        ...

    def contains_all(self, match: Collection[Any]) -> builtins.bool:
        """Checks if all elements in the specified collection are contained in this collection."""
        ...

    def distinct(self) -> _List[Any]:
        """Returns a collection containing only distinct elements from the given collection."""
        ...

    def drop(self, items: builtins.int) -> _List[Any]:
        """Returns a list containing all elements except first n elements."""
        ...

    def drop_last(self, items: builtins.int) -> _List[Any]:
        """Returns a list containing all elements except last n elements."""
        ...

    def element_at(self, index: builtins.int) -> Any:
        """Returns an element at the given index or throws an exception if the index is out of bounds of this collection."""
        ...

    def element_at_or_null(self, index: builtins.int) -> Union[Any, None]:
        """Returns an element at the given index or null if the index is out of bounds of this collection."""
        ...

    def element_at_or_else(
        self, index: builtins.int, defaultValue: Callable[[builtins.int], Any]
    ) -> Any:
        """Returns an element at the given index or the result of calling the defaultValue function if the index is out of bounds."""
        ...

    def find(self, predicate: Callable[[Any], bool]) -> Union[Any, None]:
        """Returns the first element matching the given predicate, or null if no such element was found."""
        ...

    def first(self) -> Any:
        """Returns the first element."""
        ...

    def first_not_null(self) -> Union[Any, None]:
        """Returns the first element that is not null."""
        ...

    def first_or_null(self) -> Union[Any, None]:
        """Returns the first element or null if the map is empty."""
        ...

    def plus(self, other: Any) -> _Dict[Any, Any]:
        """Returns a list containing all elements of the original collection and then all elements of the given elements."""
        ...

    def count_(self) -> builtins.int:
        """Returns the number of elements in this collection."""
        ...

Map: TypeAlias = kt_map

def map_of(items: dict) -> kt_map: ...
def empty_map() -> kt_map: ...
