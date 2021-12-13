from ..utils import int_or_none as int_or_none, parse_age_limit as parse_age_limit, smuggle_url as smuggle_url, unescapeHTML as unescapeHTML
from .brightcove import BrightcoveNewIE as BrightcoveNewIE
from .common import InfoExtractor as InfoExtractor

class VrakIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str
