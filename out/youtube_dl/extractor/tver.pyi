from ..compat import compat_str as compat_str
from ..utils import int_or_none as int_or_none, remove_start as remove_start, smuggle_url as smuggle_url, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class TVerIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str
