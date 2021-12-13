from ..compat import compat_HTTPError as compat_HTTPError, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, int_or_none as int_or_none, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, qualities as qualities, try_get as try_get, update_url_query as update_url_query, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class TVPlayIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class ViafreeIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...

class TVPlayHomeIE(InfoExtractor): ...
