from ..compat import compat_str as compat_str
from ..utils import js_to_json as js_to_json, parse_duration as parse_duration, parse_iso8601 as parse_iso8601
from .common import InfoExtractor as InfoExtractor

class RDSIE(InfoExtractor):
    IE_DESC: str
