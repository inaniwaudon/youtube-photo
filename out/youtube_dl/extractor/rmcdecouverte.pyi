from ..compat import compat_parse_qs as compat_parse_qs, compat_urlparse as compat_urlparse
from ..utils import smuggle_url as smuggle_url
from .brightcove import BrightcoveLegacyIE as BrightcoveLegacyIE
from .common import InfoExtractor as InfoExtractor

class RMCDecouverteIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str
