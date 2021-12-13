from ..compat import compat_str as compat_str, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class LyndaBaseIE(InfoExtractor): ...

class LyndaIE(LyndaBaseIE):
    IE_NAME: str
    IE_DESC: str

class LyndaCourseIE(LyndaBaseIE):
    IE_NAME: str
    IE_DESC: str
