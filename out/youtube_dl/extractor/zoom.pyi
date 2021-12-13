from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, js_to_json as js_to_json, parse_filesize as parse_filesize, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class ZoomIE(InfoExtractor):
    IE_NAME: str
