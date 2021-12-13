from ..compat import compat_str as compat_str
from ..utils import dict_get as dict_get, int_or_none as int_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class ABCOTVSIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class ABCOTVSClipsIE(InfoExtractor):
    IE_NAME: str
