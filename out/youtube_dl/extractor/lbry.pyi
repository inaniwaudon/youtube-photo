from ..compat import compat_parse_qs as compat_parse_qs, compat_str as compat_str, compat_urllib_parse_unquote as compat_urllib_parse_unquote, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, determine_ext as determine_ext, int_or_none as int_or_none, mimetype2ext as mimetype2ext, try_get as try_get, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class LBRYBaseIE(InfoExtractor): ...

class LBRYIE(LBRYBaseIE):
    IE_NAME: str

class LBRYChannelIE(LBRYBaseIE):
    IE_NAME: str
