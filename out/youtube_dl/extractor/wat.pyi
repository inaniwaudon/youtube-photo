from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, try_get as try_get, unified_strdate as unified_strdate
from .common import InfoExtractor as InfoExtractor

class WatIE(InfoExtractor):
    IE_NAME: str
