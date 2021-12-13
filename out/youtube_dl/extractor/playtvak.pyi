from ..compat import compat_urllib_parse_urlencode as compat_urllib_parse_urlencode, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, qualities as qualities
from .common import InfoExtractor as InfoExtractor

class PlaytvakIE(InfoExtractor):
    IE_DESC: str
