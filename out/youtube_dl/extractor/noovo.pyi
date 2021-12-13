from ..compat import compat_str as compat_str
from ..utils import int_or_none as int_or_none, js_to_json as js_to_json, smuggle_url as smuggle_url, try_get as try_get
from .brightcove import BrightcoveNewIE as BrightcoveNewIE
from .common import InfoExtractor as InfoExtractor

class NoovoIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str
