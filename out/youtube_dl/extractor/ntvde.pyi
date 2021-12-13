from ..compat import compat_urlparse as compat_urlparse
from ..utils import int_or_none as int_or_none, js_to_json as js_to_json, parse_duration as parse_duration
from .common import InfoExtractor as InfoExtractor

class NTVDeIE(InfoExtractor):
    IE_NAME: str
