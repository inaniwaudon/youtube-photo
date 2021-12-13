from ..compat import compat_str as compat_str
from ..utils import smuggle_url as smuggle_url, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class PlayStuffIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str
