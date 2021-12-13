from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_iso8601 as parse_iso8601
from .common import InfoExtractor as InfoExtractor

class PlayFMIE(InfoExtractor):
    IE_NAME: str
