from ..utils import int_or_none as int_or_none, js_to_json as js_to_json, orderedSet as orderedSet, parse_duration as parse_duration, sanitized_Request as sanitized_Request, str_to_int as str_to_int, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class XTubeIE(InfoExtractor): ...

class XTubeUserIE(InfoExtractor):
    IE_DESC: str
