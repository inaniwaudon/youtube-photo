from ..compat import compat_parse_qs as compat_parse_qs, compat_str as compat_str, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, qualities as qualities, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class SixPlayIE(InfoExtractor):
    IE_NAME: str
