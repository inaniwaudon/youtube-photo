from ..compat import compat_str as compat_str, compat_urlparse as compat_urlparse
from ..utils import extract_attributes as extract_attributes, float_or_none as float_or_none, int_or_none as int_or_none, try_get as try_get, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class TEDIE(InfoExtractor):
    IE_NAME: str
