from .compat import compat_str as compat_str, compat_struct_unpack as compat_struct_unpack
from .utils import ExtractorError as ExtractorError
from typing import Any

class _AVMClass_Object:
    avm_class: Any
    def __init__(self, avm_class) -> None: ...

class _ScopeDict(dict):
    avm_class: Any
    def __init__(self, avm_class) -> None: ...

class _AVMClass:
    name_idx: Any
    name: Any
    method_names: Any
    method_idxs: Any
    methods: Any
    method_pyfunctions: Any
    static_properties: Any
    variables: Any
    constants: Any
    def __init__(self, name_idx, name, static_properties: Any | None = ...) -> None: ...
    def make_object(self): ...
    def register_methods(self, methods) -> None: ...

class _Multiname:
    kind: Any
    def __init__(self, kind) -> None: ...

StringClass: Any
ByteArrayClass: Any
TimerClass: Any
TimerEventClass: Any

class _Undefined:
    def __bool__(self): ...
    __nonzero__: Any
    def __hash__(self): ...

undefined: Any

class SWFInterpreter:
    constant_ints: Any
    constant_uints: Any
    constant_strings: Any
    multinames: Any
    def __init__(self, file_contents): ...
    def patch_function(self, avm_class, func_name, f) -> None: ...
    def extract_class(self, class_name, call_cinit: bool = ...): ...
    def extract_function(self, avm_class, func_name): ...
