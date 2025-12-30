# PyKotlin

PyKotlin is a Python library designed to **bridge the syntax gap between Python and Kotlin**. It brings the expressive and fluent API of Kotlin's standard library to Python, making Python code feel more familiar to Kotlin developers and providing all Pythonistas with powerful new ways to manipulate strings, collections, and more.

## The Goal

The primary goal of this project is to reduce cognitive friction for developers moving between Python and Kotlin. Python and Kotlin share many conceptual similarities, but their syntax for common operations (especially collection manipulation and string handling) differs significantly.

PyKotlin bridges this gap by:
1.  **Injecting Fluent APIs**: Adding Kotlin's expressive method names directly to Python's built-in types.
2.  **Standardizing API Surface**: Providing a consistent experience that mirrors the Kotlin Standard Library.
3.  **Enhancing Readability**: Allowing for chainable operations that read more like natural language or Kotlin code.
4. **Making You Feel At Home**: Allowing you to write code that feels more like Kotlin.

## Key Features

- **Fluent Standard Library**: Use Kotlin's method names on Python built-ins.
  - Strings: `.uppercase()`, `.lowercase()`, `.take(n)`, `.to_int_or_null()`, `.is_null_or_blank()`.
  - Lists: `.filter()`, `.map()`, `.flatten()`, `.first_or_null()`, `.distinct()`.
- **Extension Functions**: Define your own extensions on any class (including built-ins) using the `@extension` decorator.
- **Null Safety Helpers**: Methods like `to_int_or_null()` and `first_or_null()` provide a more "Kotlin-esque" way to handle potential missing values.
- **Type Aliases**: Familiar Kotlin type names like `String`, `Int`, `Boolean`, `List`, and `Map` are available.

## Naming Conventions

While PyKotlin brings Kotlin's API to Python, it intentionally follows **Python's snake_case naming conventions** for all injected functions, methods, and extensions.

This design choice ensures that:
1.  **Python Consistency**: Code remains idiomatic to the Python ecosystem.
2.  **Developer Portability**: Developers moving between PyKotlin and standard Python projects stay familiar with Python's style conventions, making their skills more portable.
3.  **Tooling Compatibility**: Auto-completion and linting tools behave as expected in a Python environment.

For example, Kotlin's `toIntOrNull()` becomes Python's `to_int_or_null()`.

## How it Works

PyKotlin uses "injection" (via the `forbiddenfruit` library) to add methods directly to Python's built-in classes at runtime. This allows you to call these methods as if they were natively part of Python.

### Basic Usage

Simply import the library to activate the injections:

```python
import pykotlin

# String manipulations
name = "   pykotlin   "
print(name.trim().uppercase().take(2)) # Output: PY

# Collection manipulations
numbers = [1, 2, 3, 4, 5]
evens = numbers.filter_(lambda x: x % 2 == 0)
print(evens) # Output: [2, 4]

# Null-safe conversions
num = "123".to_int_or_null() # 123
invalid = "abc".to_int_or_null() # None
```

### Creating Extensions

You can add your own methods to existing classes:

```python
from pykotlin import extension

@extension(str)
def shout(self):
    return self.upper() + "!!!"

print("hello".shout()) # Output: HELLO!!!
```

## Disclaimer

PyKotlin uses advanced monkey-patching techniques to modify built-in types. While this provides a powerful and seamless experience, it should be used with an understanding of how it affects the global Python environment.

---

*Bridge the gap. Write PyKotlin.*
