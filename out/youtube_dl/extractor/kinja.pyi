from ..compat import compat_str as compat_str, compat_urllib_parse_unquote as compat_urllib_parse_unquote
from ..utils import int_or_none as int_or_none, parse_iso8601 as parse_iso8601, strip_or_none as strip_or_none, try_get as try_get, unescapeHTML as unescapeHTML, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class KinjaEmbedIE(InfoExtractor):
    IENAME: str
