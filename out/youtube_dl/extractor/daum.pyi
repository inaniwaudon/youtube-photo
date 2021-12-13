from ..compat import compat_parse_qs as compat_parse_qs, compat_urllib_parse_unquote as compat_urllib_parse_unquote, compat_urlparse as compat_urlparse
from .common import InfoExtractor as InfoExtractor

class DaumBaseIE(InfoExtractor): ...

class DaumIE(DaumBaseIE):
    IE_NAME: str

class DaumClipIE(DaumBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class DaumListIE(InfoExtractor): ...

class DaumPlaylistIE(DaumListIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class DaumUserIE(DaumListIE):
    IE_NAME: str
