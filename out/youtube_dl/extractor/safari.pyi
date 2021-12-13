from ..compat import compat_parse_qs as compat_parse_qs, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, update_url_query as update_url_query
from .common import InfoExtractor as InfoExtractor

class SafariBaseIE(InfoExtractor):
    LOGGED_IN: bool

class SafariIE(SafariBaseIE):
    IE_NAME: str
    IE_DESC: str

class SafariApiIE(SafariBaseIE):
    IE_NAME: str

class SafariCourseIE(SafariBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...
