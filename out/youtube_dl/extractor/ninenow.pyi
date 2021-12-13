from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none, smuggle_url as smuggle_url
from .common import InfoExtractor as InfoExtractor

class NineNowIE(InfoExtractor):
    IE_NAME: str
    BRIGHTCOVE_URL_TEMPLATE: str
