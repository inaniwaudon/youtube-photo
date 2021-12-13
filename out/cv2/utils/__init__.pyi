from typing import Any, NamedTuple

class NativeMethodPatchedResult(NamedTuple):
    py: Any
    native: Any

def testOverwriteNativeMethod(arg): ...
