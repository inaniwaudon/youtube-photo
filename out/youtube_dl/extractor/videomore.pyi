from ..compat import compat_parse_qs as compat_parse_qs, compat_str as compat_str, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none
from .common import InfoExtractor as InfoExtractor

class VideomoreBaseIE(InfoExtractor): ...

class VideomoreIE(InfoExtractor):
    IE_NAME: str

class VideomoreVideoIE(VideomoreBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class VideomoreSeasonIE(VideomoreBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
