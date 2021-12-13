from ..compat import compat_parse_qs as compat_parse_qs, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import HEADRequest as HEADRequest, determine_ext as determine_ext, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, strip_or_none as strip_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class IGNBaseIE(InfoExtractor): ...

class IGNIE(IGNBaseIE):
    IE_NAME: str

class IGNVideoIE(InfoExtractor): ...
class IGNArticleIE(IGNBaseIE): ...
