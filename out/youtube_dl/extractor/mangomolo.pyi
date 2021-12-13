from ..compat import compat_b64decode as compat_b64decode, compat_urllib_parse_unquote as compat_urllib_parse_unquote
from ..utils import int_or_none as int_or_none
from .common import InfoExtractor as InfoExtractor
from typing import Any

class MangomoloBaseIE(InfoExtractor): ...

class MangomoloVideoIE(MangomoloBaseIE):
    IE_NAME: Any

class MangomoloLiveIE(MangomoloBaseIE):
    IE_NAME: Any
