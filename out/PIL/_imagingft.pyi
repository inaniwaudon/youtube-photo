from typing import Any

HAVE_FRIBIDI: bool
HAVE_HARFBUZZ: bool
HAVE_RAQM: bool
freetype2_version: str
fribidi_version: str
harfbuzz_version: str
raqm_version: str

def getfont(*args, **kwargs) -> Any: ...
