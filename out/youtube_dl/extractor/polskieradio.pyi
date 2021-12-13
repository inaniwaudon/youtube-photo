from ..compat import compat_str as compat_str, compat_urllib_parse_unquote as compat_urllib_parse_unquote, compat_urlparse as compat_urlparse
from ..utils import extract_attributes as extract_attributes, int_or_none as int_or_none, strip_or_none as strip_or_none, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class PolskieRadioIE(InfoExtractor): ...

class PolskieRadioCategoryIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
