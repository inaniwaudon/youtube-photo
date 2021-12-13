from ..compat import compat_HTTPError as compat_HTTPError, compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none, parse_resolution as parse_resolution, str_or_none as str_or_none, try_get as try_get, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class PuhuTVIE(InfoExtractor):
    IE_NAME: str

class PuhuTVSerieIE(InfoExtractor):
    IE_NAME: str
