from ..compat import compat_str as compat_str
from ..utils import float_or_none as float_or_none, try_get as try_get, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class CCTVIE(InfoExtractor):
    IE_DESC: str
