from ..compat import compat_parse_qs as compat_parse_qs, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import float_or_none as float_or_none, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, remove_start as remove_start
from .common import InfoExtractor as InfoExtractor

class ArnesIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
