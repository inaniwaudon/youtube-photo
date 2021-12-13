from ..compat import compat_HTTPError as compat_HTTPError
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, parse_iso8601 as parse_iso8601
from .common import InfoExtractor as InfoExtractor

class ThreeQSDNIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
