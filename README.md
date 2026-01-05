# **Kothonic**

> "Write Kotlin\* in Python"

Kothonic bridges the gap between Python and Kotlin, pushing the limits of the Python language to give users a way to write Kotlin-like code in Python projects.

## Why Kothonic?

> "Once you go Kotlin you never go back."

*   **Fluent Chaining**: Read your code from left to right. Chain operations naturally without jumping back and forth between function calls.
*   **Null Safety**: Handle missing data gracefully. Use methods like `to_int_or_null()` to avoid unexpected crashes and excessive `try/except` blocks.
*   **Expressive Collections**: Unleash the full power of collection processing. `filter()`, `map()`, `flatten()`, and `find()` elements in your lists and dictionaries with an intuitive, unified API.
*   **Scoping Functions**: Keep your scope clean and your intent clear with `let()`, and `apply()`.
*   **The Power of `it`**: Simplify your lambdas. Access the current element in a concise and readable way.
*   **Modular**: Every Kothonic code is valid Python so you can take only the features you are really missing.

## Features

> "Omg you can do that!?"

Some great features of Kothonic are:

### String Manipulation
Perform complex string operations with ease and safety.

```python
# Kothonic
raw_string = String("  123  ")
result = raw_string.trim().to_int_or_null() # result is 123 (an integer)
```

### Collection Pipelines
Process data utilizing a powerful, functional approach.

```python
from kothonic.collections import List

users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True}
]

users = List(users)

# Get names of active users calling standard Python dict access
active_names = users.filter_(lambda u: u['active']).map_(lambda u: u['name'])
# ['Alice', 'Charlie']
```

### Safety First
Avoid runtime errors with safe conversion methods.

**Pythonic way:**
```python
try:
    value = int(user_input)
except ValueError:
    value = None
```

**Kothonic way:**
```python
value = user_input.to_int_or_null()
```

## Getting Started

### Installation

```bash
pip install kothonic
```

### Usage

You can start using Kothonic's features immediately by importing the provided classes.

```python
from kothonic import String

s = String("   hello   ")
print(s.trim().uppercase()) # HELLO
```

## Disclaimer

A **completely optional** use of Kothonic is achieving "native integration" through advanced monkey-patching of Python's built-in types (`str`, `int`, `list`, etc). This can make the existing types work at runtime with methods such as `int.to_float()`. While this provides a powerful and "native" feel, it modifies the runtime environment. This is safe so long as no pre-existing methods of the classes are patched which will actively be monitored. 

If you're unsure about how this works please take the time to look into **forbiddenfruit**. 

Or if you're unsure just stick with the extended classes that are part of Kothonic (`String`, `Int`, `List`, etc) which behave exactly like the standard types but have the benefits of Kotlin.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


