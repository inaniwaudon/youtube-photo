from .compat import compat_expanduser as compat_expanduser, compat_get_terminal_size as compat_get_terminal_size, compat_getenv as compat_getenv, compat_kwargs as compat_kwargs, compat_shlex_split as compat_shlex_split
from .downloader.external import list_external_downloaders as list_external_downloaders
from .utils import preferredencoding as preferredencoding, write_string as write_string
from typing import Any

def parseOpts(overrideArguments: Any | None = ...): ...
