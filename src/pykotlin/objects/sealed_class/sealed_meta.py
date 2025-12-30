from typing import Dict
from typing import MutableMapping
from typing import Any
from typing import Tuple
class SealedMeta(type):
    """
    Metaclass for Kt_Sealed that allows nested classes to inherit
    from their parent sealed class during definition.
    """
    @classmethod
    def __prepare__(metacls, name: str, bases: Tuple[type, ...], **kwargs: Any) -> MutableMapping[str, Any]:
        # Provide a placeholder for the class being defined.
        # This allows: class MySealed(Kt_Sealed): class Internal(MySealed): ...
        class SealedPlaceholder:
            pass
        return {name: SealedPlaceholder}

    def __new__(mcs, name: str, bases: Tuple[type, ...], namespace: Dict[str, Any], **kwargs: Any) -> type:
        # Extract the placeholder we injected in __prepare__
        placeholder = namespace.get(name)
        
        # Create the actual class
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        
        # Patch nested classes
        for attr_name, attr_value in namespace.items():
            if isinstance(attr_value, type):
                # We patch classes that inherited from either the placeholder (legacy/runtime hack)
                # or Kt_Sealed directly (recommended way for static analysis).
                is_placeholder_base = (placeholder is not None and placeholder in attr_value.__bases__)
                
                # Check for Kt_Sealed in bases without referencing it by name yet
                # We can check if any base's name is 'Kt_Sealed' or if it's an instance of mcs
                is_kt_sealed_base = False
                if attr_name != name:
                    for base in attr_value.__bases__:
                        if base.__name__ == "Kt_Sealed":
                            is_kt_sealed_base = True
                            break

                if is_placeholder_base or is_kt_sealed_base:
                    # Replace the placeholder or Kt_Sealed with the real class in the bases
                    new_bases = tuple(
                        cls if (b is placeholder or b.__name__ == "Kt_Sealed") else b 
                        for b in attr_value.__bases__
                    )
                    try:
                        attr_value.__bases__ = new_bases
                    except TypeError:
                        # Fallback for classes that don't allow __bases__ modification
                        pass
                    
        return cls
