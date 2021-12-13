from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, int_or_none as int_or_none, js_to_json as js_to_json, mimetype2ext as mimetype2ext, parse_iso8601 as parse_iso8601, try_get as try_get, unescapeHTML as unescapeHTML
from .common import InfoExtractor as InfoExtractor

class DVTVIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
