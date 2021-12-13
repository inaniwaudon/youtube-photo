from ..utils import compat_str as compat_str, float_or_none as float_or_none, int_or_none as int_or_none, smuggle_url as smuggle_url, str_or_none as str_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class STVPlayerIE(InfoExtractor):
    IE_NAME: str
    BRIGHTCOVE_URL_TEMPLATE: str
