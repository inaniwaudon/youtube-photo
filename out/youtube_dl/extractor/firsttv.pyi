from ..compat import compat_str as compat_str, compat_urlparse as compat_urlparse
from ..utils import int_or_none as int_or_none, qualities as qualities, unified_strdate as unified_strdate, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class FirstTVIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
