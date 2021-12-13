from ..compat import compat_str as compat_str, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, js_to_json as js_to_json, strip_jsonp as strip_jsonp, try_get as try_get, unified_strdate as unified_strdate, update_url_query as update_url_query, url_or_none as url_or_none, urlhandle_detect_ext as urlhandle_detect_ext
from .common import InfoExtractor as InfoExtractor

class WDRIE(InfoExtractor): ...
class WDRPageIE(InfoExtractor): ...
class WDRElefantIE(InfoExtractor): ...

class WDRMobileIE(InfoExtractor):
    IE_NAME: str
