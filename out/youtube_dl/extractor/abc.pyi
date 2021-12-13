from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, js_to_json as js_to_json, parse_iso8601 as parse_iso8601, try_get as try_get, unescapeHTML as unescapeHTML, update_url_query as update_url_query
from .common import InfoExtractor as InfoExtractor

class ABCIE(InfoExtractor):
    IE_NAME: str

class ABCIViewIE(InfoExtractor):
    IE_NAME: str
